package com.example.imageapp.image.service;

import java.io.IOException;
import java.io.InputStream;
import java.nio.charset.StandardCharsets;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;


@Service
public class ImageValidService {

    private static final byte[] JPEG_SIGNATURE = new byte[]{(byte) 0xFF, (byte) 0xD8, (byte) 0xFF};
    private static final byte[] PNG_SIGNATURE = new byte[]{(byte) 0x89, (byte) 0x50, (byte) 0x4E, (byte) 0x47};

    private boolean isJpegHeader(byte[] header) {
        if (header.length < JPEG_SIGNATURE.length) {
            return false;
        }
        for (int i = 0; i < JPEG_SIGNATURE.length; i++) {
            if (header[i] != JPEG_SIGNATURE[i]) {
                return false;
            }
        }
        return true;
    }

    private boolean isPngHeader(byte[] header) {
        if (header.length < PNG_SIGNATURE.length) {
            return false;
        }
        for (int i = 0; i < PNG_SIGNATURE.length; i++) {
            if (header[i] != PNG_SIGNATURE[i]) {
                return false;
            }
        }
        return true;

    }

    public boolean isValidImage(MultipartFile file) {
        try (InputStream is = file.getInputStream()) {
            byte[] header = new byte[8];
            is.read(header, 0, header.length);
            if (isPngHeader(header) || isJpegHeader(header)) {

                byte[] fileBytes = is.readAllBytes();
                String fileContent = new String(fileBytes, StandardCharsets.UTF_8);
            
                // Preventing Web Shell
                if (fileContent.contains("Runtime") ||
                    fileContent.contains("File") || 
                    fileContent.contains("exec")) {
                    return false;
                }

                return true;
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return false;
    }

}