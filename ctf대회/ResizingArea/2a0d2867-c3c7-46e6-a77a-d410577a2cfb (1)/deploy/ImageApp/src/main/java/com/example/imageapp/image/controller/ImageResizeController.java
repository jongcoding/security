package com.example.imageapp.image.controller;

import com.example.imageapp.image.service.ImageResizeService;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
@RequestMapping("/image")
public class ImageResizeController {
    @GetMapping("/resize")
    public String showResizeForm(Model model){
        return "resize";
    }
}
