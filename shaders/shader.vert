# version 450

layout(binding = 0) uniform UniformBufferObject {
    mat4 model;
} ubo;

layout(std430, binding = 1) buffer StorageBuffer {
    mat4 model[];
};

layout(location = 0) in vec2 inPosition;
layout(location = 1) in vec3 inColor;

layout(location = 0) out vec3 fragColor;

void main() {
    mat4 modelMatrix = model[gl_InstanceIndex];
    gl_Position = modelMatrix * vec4(inPosition, 0.0, 1.0);
    fragColor = inColor;
}