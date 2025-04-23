@echo off

echo "Building shaders..."

%VULKAN_SDK%/Bin/glslc.exe shaders/shader.frag -o shaders/shader.frag.spv
%VULKAN_SDK%/Bin/glslc.exe shaders/shader.vert -o shaders/shader.vert.spv

call "C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvars64.bat"

SET includes=/Isrc /I%VULKAN_SDK%/Include /IC:/Users/chris/Source/glfw-3.4.bin.WIN64/include /IC:/Users/chris/Source/glm-1.0.1-light
SET links=/link /LIBPATH:%VULKAN_SDK%/Lib /LIBPATH:C:/Users/chris/Source/glfw-3.4.bin.WIN64/lib-vc2022 user32.lib gdi32.lib shell32.lib vulkan-1.lib glfw3.lib 
SET defines=/D DEBUG /D WINDOWS_BUILD

echo "Building main..."

cl /MD /EHsc /Z7 /std:c++17 /Fe"build/main" %includes% %defines% src/main.cpp %links%
