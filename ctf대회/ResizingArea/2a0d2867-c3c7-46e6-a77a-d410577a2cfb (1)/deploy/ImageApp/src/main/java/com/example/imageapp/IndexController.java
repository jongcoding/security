package com.example.imageapp;

import com.example.imageapp.util.JwtUtil;
import jakarta.servlet.http.Cookie;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;


@Controller
@RequestMapping("/")
public class IndexController {

    private final JwtUtil jwtUtil;

    @Autowired
    public IndexController(JwtUtil jwtUtil) {
        this.jwtUtil = jwtUtil;
    }

    @GetMapping("/")
    public String showForm() {
        return "index";
    }

    @PostMapping("/")
    public String addName(@RequestParam String name, HttpServletResponse response, RedirectAttributes redirectAttributes) {
        String jwt = jwtUtil.generateToken(name);
        Cookie jwtCookie = new Cookie("Authorization", jwt);
        jwtCookie.setHttpOnly(true);
        jwtCookie.setPath("/");
        response.addCookie(jwtCookie);
        return "redirect:/image/upload";
    }
}

