glslc shaders/shader.frag -o shaders/shader.frag.spv
glslc shaders/shader.vert -o shaders/shader.vert.spv

clang++ -std=c++17 -stdlib=libc++ -target arm64-apple-macos \
    -I$VULKAN_SDK/include \
    -I/opt/homebrew/include \
    -L$VULKAN_SDK/lib \
    -L/opt/homebrew/lib \
    src/main.cpp -o build/main \
    -lvulkan.1 -lglfw \
    -framework Cocoa -framework QuartzCore -framework Metal -framework IOKit