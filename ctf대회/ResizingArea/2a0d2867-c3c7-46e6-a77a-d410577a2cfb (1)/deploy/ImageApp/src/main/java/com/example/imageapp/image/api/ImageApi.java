package com.example.imageapp.image.api;

import javax.imageio.ImageIO;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.net.MalformedURLException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.HashMap;
import java.util.Map;

import com.example.imageapp.image.service.ImageResizeService;
import jakarta.annotation.PostConstruct;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.HttpHeaders;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.core.io.UrlResource;

@Controller
@RequestMapping("/api/image")
public class ImageApi {

    @Value("${file.upload-dir}")
    private String uploadDir;

    private final ImageResizeService imageResizeService;

    public ImageApi(ImageResizeService imageResizeService) {
        this.imageResizeService = imageResizeService;
    }

    @PostConstruct
    public void init() {
        String currentDir = System.getProperty("user.dir");
        File dir = new File(currentDir);
        if (!dir.isAbsolute()) {
            uploadDir = new File(currentDir, uploadDir).getAbsolutePath();
        }
    }

    @PostMapping("resize")
    public ResponseEntity<Map<String, Object>> doResize(
            @RequestParam("filename") String filename,
            @RequestParam("width") int width,
            @RequestParam("height") int height) throws IOException {

        Map<String, Object> response = new HashMap<>();

        String cmd = "/bin/cp" + " " + uploadDir + "/" + filename + " " + "/tmp";
        Process p = null;
        try {
            p = Runtime.getRuntime().exec(cmd);
            p.waitFor();
        } catch (InterruptedException e) {
            throw new RuntimeException("Error: " + e.getMessage());

        }

        if ((width <= 0 || width >= 1024) || (height <= 0) || height >= 1024) {
            response.put("result", "fail");
            response.put("message", "Out of range");
            response.put("downloadUrl", null);
            return ResponseEntity.status(500).body(response);
        }

        File file = new File(uploadDir + "/" + filename);

        try {
            BufferedImage originalImage = ImageIO.read(file);
            Image resizedImage = originalImage.getScaledInstance(width, height, Image.SCALE_SMOOTH);

            BufferedImage newImage = new BufferedImage(width, height, BufferedImage.TYPE_INT_ARGB);
            Graphics2D g2d = newImage.createGraphics();
            g2d.drawImage(resizedImage, 0, 0, null);
            g2d.dispose();

            File outputFile = new File("/tmp" + "/" + "resized_" + file.getName());
            ImageIO.write(newImage, file.getName().substring(file.getName().lastIndexOf('.') + 1), outputFile);
            response.put("result", "success");
            response.put("message", "Image resized successfully");
            // ** TODO: Add SHA256 **
            response.put("downloadUrl", "/api/image/download?filename=resized_" + file.getName());
            return ResponseEntity.ok(response);

        } catch (IOException e) {
            response.put("result", "error");
            response.put("message", "Error resizing the image.");
            response.put("downloadUrl", null);

            return ResponseEntity.status(500).body(response);
        }

    }

    @GetMapping("/download")
    public ResponseEntity<UrlResource> doDownload(@RequestParam("filename") String filename) {
        Map<String, Object> response = new HashMap<>();
        if (!filename.matches("^resized_[0-9a-f]{64}\\.(jpg|jpeg|png)$")) {
            return ResponseEntity.badRequest().body(null);
        }
        try {
            Path filePath = Paths.get("/tmp").resolve(filename).normalize();
            UrlResource resource = new UrlResource(filePath.toUri());

            if (resource.exists() && resource.isReadable()) {
                String contentType = Files.probeContentType(filePath);

                return ResponseEntity.ok()
                        .contentType(org.springframework.http.MediaType.parseMediaType(contentType))
                        .header(HttpHeaders.CONTENT_DISPOSITION, "attachment; filename=\"" + resource.getFilename() + "\"")
                        .body(resource);
            } else {
                throw new RuntimeException("File not found: " + filename);
            }
        } catch (MalformedURLException e) {
            throw new RuntimeException("Error: " + e.getMessage());
        } catch (IOException e) {
            throw new RuntimeException("Error: " + e.getMessage());
        }
    }


}
