package com.example.imageapp.image.controller;

import com.example.imageapp.image.service.ImageValidService;
import com.example.imageapp.util.JwtUtil;
import jakarta.annotation.PostConstruct;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

import java.io.File;
import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;

@Controller
@RequestMapping("/image")
public class ImageUploadController {

    @Value("${file.upload-dir}")
    private String uploadDir;

    private static final int SALT_LENGTH = 8;
    private static final String CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@$%^&*";

    private final ImageValidService imageValidService;
    private final JwtUtil jwtUtil;

    public ImageUploadController(ImageValidService imageValidService, JwtUtil jwtUtil) {
        this.imageValidService = imageValidService;
        this.jwtUtil = jwtUtil;
    }

    @PostConstruct
    public void init() {
        String currentDir = System.getProperty("user.dir");
        File dir = new File(uploadDir);
        if (!dir.isAbsolute()) {
            uploadDir = new File(currentDir, uploadDir).getAbsolutePath();
        }
        new File(uploadDir).mkdirs();
    }

    private String SHA256(String input, String salt) throws NoSuchAlgorithmException {
        MessageDigest md = MessageDigest.getInstance("SHA-256");
        md.update(salt.getBytes());
        byte[] hashedBytes = md.digest(input.getBytes());
        return bytesToHex(hashedBytes);

    }

    private String bytesToHex(byte[] bytes) {
        StringBuilder hexString = new StringBuilder(2 * bytes.length);
        for (byte b : bytes) {
            String hex = Integer.toHexString(0xff & b);
            if (hex.length() == 1) {
                hexString.append('0');
            }
            hexString.append(hex);
        }
        return hexString.toString();
    }

    private String generateSalt() {
        SecureRandom random = new SecureRandom();
        StringBuilder salt = new StringBuilder(SALT_LENGTH);

        for (int i = 0; i < SALT_LENGTH; i++) {
            int index = random.nextInt(CHARACTERS.length());
            salt.append(CHARACTERS.charAt(index));
        }

        return salt.toString();
    }

    @GetMapping("/upload")
    public String showUploadForm() {
        return "upload";
    }

    @PostMapping("/upload")
    public String doFileUpload(@RequestParam("file") MultipartFile file, RedirectAttributes redirectAttributes) {
        if (file.isEmpty()) {
            redirectAttributes.addFlashAttribute("message", "File is empty");
            return "redirect:/image/upload";
        }
        String fileName = file.getOriginalFilename();
        if (fileName != null) {
            if (!fileName.matches("^[a-zA-Z0-9_.-]+$")) {
                redirectAttributes.addFlashAttribute("message", "Invalid file name");
                return "redirect:/image/upload";
            }
            String fileExtension = fileName.substring(fileName.lastIndexOf(".") + 1).toLowerCase();
            if (!fileExtension.equals("jpg") && !fileExtension.equals("jpeg") && !fileExtension.equals("png")) {
                redirectAttributes.addFlashAttribute("message", "Invalid file extension");
                return "redirect:/image/upload";
            }
            if (!imageValidService.isValidImage(file)) {
                redirectAttributes.addFlashAttribute("message", "Invalid image format");
                return "redirect:/image/upload";
            }

        } else {
            redirectAttributes.addFlashAttribute("message", "File is empty");
            return "redirect:/image/upload";
        }

        try {
            // ** Add SHA256 for security **
            String name = fileName.substring(0, fileName.lastIndexOf('.'));
            String ext = fileName.substring(fileName.lastIndexOf('.'));
            String secret = generateSalt();
            String hashedName = SHA256(name, secret);
            Path path = Paths.get(uploadDir, hashedName + ext);
            file.transferTo(path.toFile());
            redirectAttributes.addFlashAttribute("filename", file.getOriginalFilename());
            return "redirect:/image/resize";
        } catch (IOException | NoSuchAlgorithmException e) {
            e.printStackTrace();
            redirectAttributes.addFlashAttribute("message", "File upload failed");
            return "redirect:/image/upload";
        }
    }
}
