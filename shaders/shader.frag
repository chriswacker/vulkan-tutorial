#version 450

layout(location = 0) in vec3 fragColor;
layout(location = 1) in vec3 fragNormal;

layout(location = 0) out vec4 outColor;

void main() {
    vec3 lightDir = normalize(vec3(1.0, -1.0, 0.0));
    vec3 normal = normalize(fragNormal);
    float diffuse = max(dot(normal, -lightDir), 0.0);

    vec3 finalColor = fragColor * (0.2 + 0.8 * diffuse); // Add ambient

    // vec3 finalColor = normal;

    outColor = vec4(finalColor, 1.0);
}
