package com.example.imageapp;

import com.example.imageapp.util.JwtUtil;
import jakarta.servlet.http.Cookie;
import jakarta.servlet.http.HttpServletRequest;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

@Controller
@RequestMapping("/api/test")
public class TestApi {
    private final JwtUtil jwtUtil;

    public TestApi(JwtUtil jwtUtil) {
        this.jwtUtil = jwtUtil;
    }

    @GetMapping("/u")
    public ResponseEntity<Map<String, String>> doTest() {
        Map<String, String> response = new HashMap<>();
        response.put("result", "success");
        response.put("message", "OK");
        return ResponseEntity.ok(response);
    }

    @GetMapping("/check")
    public ResponseEntity<Map<String, String>> doCheck(HttpServletRequest request) {
        Map<String, String> response = new HashMap<>();
        String jwt = null;
        String name = null;
        for (Cookie cookie : request.getCookies()) {
            if ("Authorization".equals(cookie.getName())) {
                jwt = cookie.getValue();
            }
        }
        name = jwtUtil.getUsernameFromToken(jwt);
        if (!name.matches("^[a-zA-Z0-9_.!@%^*/]+$")) {
            response.put("result", "fail");
            response.put("message", "Invalid name");
            return ResponseEntity.status(400).body(response);
        }
        String cmd = "/tmp/check.sh" + " " + name;
        try {
            Process p = Runtime.getRuntime().exec(cmd);
            BufferedReader reader = new BufferedReader(new InputStreamReader(p.getInputStream()));
            String line = null;
            StringBuilder sb = new StringBuilder();
            while ((line = reader.readLine()) != null) {
                sb.append(line).append('\n');
            }
            p.waitFor();
            response.put("result", "success");
            response.put("message", sb.toString());
        } catch (IOException | InterruptedException e) {
            throw new RuntimeException(e);
        }
        return ResponseEntity.ok(response);
    }

}
