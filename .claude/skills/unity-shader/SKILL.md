---
name: unity-shader
description: Create Unity shaders using Shader Graph, HLSL, or ShaderLab for Universal Render Pipeline (URP). Use when implementing custom rendering effects, materials, or visual styles.
allowed-tools: Read, Write, Edit, Glob, Grep
---



<!-- Navigation -->
**🏠 [HaroFramework Project](../../MASTER_INDEX.md)** | **📂 [Skill](./)** | **⬆️ [Skill](./)**

---
# Unity Shader Expert

Expert skill for creating shaders in Unity's Universal Render Pipeline (URP).

## When to Use This Skill

Activate this skill when the user requests:
- Custom visual effects (dissolve, hologram, water)
- Surface shaders (PBR, toon, stylized)
- Post-processing effects
- Vertex manipulation (grass, cloth, wind)
- UI shaders and effects
- Optimization of rendering

## Shader Types

### Shader Graph (Recommended for Artists)
- Visual node-based shader creation
- No code required
- URP compatible
- Easy iteration and debugging
- .shadergraph files

### HLSL Custom Function (Advanced)
- Custom code nodes in Shader Graph
- High performance
- Full control over calculations

### ShaderLab with HLSL (Full Control)
- Complete shader control
- Required for complex features
- URP shader template
- .shader files

## URP Shader Graph Template (Lit)

Create via: Right-click > Create > Shader Graph > URP > Lit Shader Graph

**Common Node Setup:**
```
Texture2D (Base Map) → Sample Texture 2D → Base Color (Output)
Texture2D (Normal Map) → Sample Texture 2D (Normal) → Normal (Output)
Float (Metallic) → Metallic (Output)
Float (Smoothness) → Smoothness (Output)
```

## URP Shader Graph Template (Unlit)

Create via: Right-click > Create > Shader Graph > URP > Unlit Shader Graph

**Simple Color Shader:**
```
Color → Base Color (Output)
Float (Alpha) → Alpha (Output)
```

## Custom Function HLSL Example

```hlsl
// Custom dissolve function
void Dissolve_float(float Progress, float NoiseValue, float EdgeWidth, out float Result)
{
    float threshold = Progress;
    float edge = EdgeWidth;

    if (NoiseValue < threshold - edge)
    {
        Result = 0.0; // Fully dissolved
    }
    else if (NoiseValue < threshold)
    {
        Result = (NoiseValue - (threshold - edge)) / edge; // Edge
    }
    else
    {
        Result = 1.0; // Solid
    }
}
```

## URP ShaderLab Template (Lit)

```hlsl
Shader "HaroFramework/CustomLit"
{
    Properties
    {
        _BaseMap("Base Map", 2D) = "white" {}
        _BaseColor("Base Color", Color) = (1, 1, 1, 1)
        _Smoothness("Smoothness", Range(0, 1)) = 0.5
        _Metallic("Metallic", Range(0, 1)) = 0
    }

    SubShader
    {
        Tags
        {
            "RenderType" = "Opaque"
            "RenderPipeline" = "UniversalPipeline"
            "Queue" = "Geometry"
        }

        Pass
        {
            Name "ForwardLit"
            Tags { "LightMode" = "UniversalForward" }

            HLSLPROGRAM
            #pragma vertex vert
            #pragma fragment frag

            // URP required keywords
            #pragma multi_compile _ _MAIN_LIGHT_SHADOWS
            #pragma multi_compile _ _ADDITIONAL_LIGHTS
            #pragma multi_compile_fragment _ _SHADOWS_SOFT

            #include "Packages/com.unity.render-pipelines.universal/ShaderLibrary/Core.hlsl"
            #include "Packages/com.unity.render-pipelines.universal/ShaderLibrary/Lighting.hlsl"

            struct Attributes
            {
                float4 positionOS : POSITION;
                float3 normalOS : NORMAL;
                float2 uv : TEXCOORD0;
            };

            struct Varyings
            {
                float4 positionHCS : SV_POSITION;
                float3 positionWS : TEXCOORD0;
                float3 normalWS : TEXCOORD1;
                float2 uv : TEXCOORD2;
            };

            TEXTURE2D(_BaseMap);
            SAMPLER(sampler_BaseMap);

            CBUFFER_START(UnityPerMaterial)
                float4 _BaseMap_ST;
                float4 _BaseColor;
                float _Smoothness;
                float _Metallic;
            CBUFFER_END

            Varyings vert(Attributes input)
            {
                Varyings output;

                VertexPositionInputs vertexInput = GetVertexPositionInputs(input.positionOS.xyz);
                VertexNormalInputs normalInput = GetVertexNormalInputs(input.normalOS);

                output.positionHCS = vertexInput.positionCS;
                output.positionWS = vertexInput.positionWS;
                output.normalWS = normalInput.normalWS;
                output.uv = TRANSFORM_TEX(input.uv, _BaseMap);

                return output;
            }

            float4 frag(Varyings input) : SV_Target
            {
                // Sample textures
                float4 baseMap = SAMPLE_TEXTURE2D(_BaseMap, sampler_BaseMap, input.uv);
                float3 albedo = baseMap.rgb * _BaseColor.rgb;

                // Lighting
                InputData lightingInput = (InputData)0;
                lightingInput.positionWS = input.positionWS;
                lightingInput.normalWS = normalize(input.normalWS);
                lightingInput.viewDirectionWS = GetWorldSpaceNormalizeViewDir(input.positionWS);
                lightingInput.shadowCoord = TransformWorldToShadowCoord(input.positionWS);

                SurfaceData surfaceData = (SurfaceData)0;
                surfaceData.albedo = albedo;
                surfaceData.metallic = _Metallic;
                surfaceData.smoothness = _Smoothness;
                surfaceData.alpha = _BaseColor.a;

                return UniversalFragmentPBR(lightingInput, surfaceData);
            }
            ENDHLSL
        }

        Pass
        {
            Name "ShadowCaster"
            Tags { "LightMode" = "ShadowCaster" }

            HLSLPROGRAM
            #pragma vertex ShadowPassVertex
            #pragma fragment ShadowPassFragment

            #include "Packages/com.unity.render-pipelines.universal/Shaders/LitInput.hlsl"
            #include "Packages/com.unity.render-pipelines.universal/Shaders/ShadowCasterPass.hlsl"
            ENDHLSL
        }
    }

    FallBack "Hidden/Universal Render Pipeline/FallbackError"
}
```

## URP ShaderLab Template (Unlit/UI)

```hlsl
Shader "HaroFramework/CustomUnlit"
{
    Properties
    {
        _MainTex("Texture", 2D) = "white" {}
        _Color("Color", Color) = (1, 1, 1, 1)
        [Enum(UnityEngine.Rendering.BlendMode)] _SrcBlend("Src Blend", Float) = 1
        [Enum(UnityEngine.Rendering.BlendMode)] _DstBlend("Dst Blend", Float) = 0
        [Enum(Off, 0, On, 1)] _ZWrite("Z Write", Float) = 1
    }

    SubShader
    {
        Tags
        {
            "RenderType" = "Opaque"
            "RenderPipeline" = "UniversalPipeline"
            "Queue" = "Geometry"
        }

        Pass
        {
            Blend [_SrcBlend] [_DstBlend]
            ZWrite [_ZWrite]

            HLSLPROGRAM
            #pragma vertex vert
            #pragma fragment frag

            #include "Packages/com.unity.render-pipelines.universal/ShaderLibrary/Core.hlsl"

            struct Attributes
            {
                float4 positionOS : POSITION;
                float2 uv : TEXCOORD0;
                float4 color : COLOR;
            };

            struct Varyings
            {
                float4 positionHCS : SV_POSITION;
                float2 uv : TEXCOORD0;
                float4 color : COLOR;
            };

            TEXTURE2D(_MainTex);
            SAMPLER(sampler_MainTex);

            CBUFFER_START(UnityPerMaterial)
                float4 _MainTex_ST;
                float4 _Color;
            CBUFFER_END

            Varyings vert(Attributes input)
            {
                Varyings output;
                output.positionHCS = TransformObjectToHClip(input.positionOS.xyz);
                output.uv = TRANSFORM_TEX(input.uv, _MainTex);
                output.color = input.color;
                return output;
            }

            float4 frag(Varyings input) : SV_Target
            {
                float4 texColor = SAMPLE_TEXTURE2D(_MainTex, sampler_MainTex, input.uv);
                return texColor * _Color * input.color;
            }
            ENDHLSL
        }
    }
}
```

## Common Shader Effects

### Dissolve Effect
```hlsl
// In Shader Graph: Custom Function Node
void DissolveEffect_float(
    float Progress,
    float NoiseValue,
    float EdgeWidth,
    float4 EdgeColor,
    out float Alpha,
    out float4 Emission)
{
    float threshold = Progress;
    float edge = EdgeWidth;

    if (NoiseValue < threshold - edge)
    {
        Alpha = 0.0;
        Emission = float4(0, 0, 0, 0);
    }
    else if (NoiseValue < threshold)
    {
        float t = (NoiseValue - (threshold - edge)) / edge;
        Alpha = t;
        Emission = EdgeColor * (1.0 - t);
    }
    else
    {
        Alpha = 1.0;
        Emission = float4(0, 0, 0, 0);
    }
}
```

### Vertex Displacement (Wind/Waves)
```hlsl
float3 ApplyWind_float(float3 positionOS, float3 normal, float time, float strength)
{
    float wave = sin(time + positionOS.x * 2.0) * cos(time * 0.5 + positionOS.z);
    float3 offset = normal * wave * strength * positionOS.y; // Affect based on height
    return positionOS + offset;
}
```

### Fresnel Effect
```hlsl
float FresnelEffect_float(float3 Normal, float3 ViewDir, float Power)
{
    return pow(1.0 - saturate(dot(normalize(Normal), normalize(ViewDir))), Power);
}
```

### Toon Shading
```hlsl
float ToonShading_float(float NdotL, int steps)
{
    float toonValue = floor(NdotL * steps) / steps;
    return toonValue;
}
```

## URP Helper Functions

```hlsl
// Transform spaces
float3 TransformObjectToWorld(float3 positionOS);
float3 TransformWorldToObject(float3 positionWS);
float4 TransformObjectToHClip(float3 positionOS);

// Normals
float3 TransformObjectToWorldNormal(float3 normalOS);
float3 TransformWorldToObjectNormal(float3 normalWS);

// View direction
float3 GetWorldSpaceViewDir(float3 positionWS);
float3 GetWorldSpaceNormalizeViewDir(float3 positionWS);

// Lighting
Light GetMainLight();
Light GetMainLight(float4 shadowCoord);
Light GetAdditionalLight(uint index, float3 positionWS);

// Shadows
float4 TransformWorldToShadowCoord(float3 positionWS);
half MainLightRealtimeShadow(float4 shadowCoord);
```

## Shader Graph Tips

### Performance Optimization
- Minimize texture samples
- Use static branches when possible
- Avoid complex math in fragment shader
- Use vertex shader for calculations when possible

### Common Nodes
- **Sample Texture 2D**: Texture sampling
- **Multiply**: Color/value multiplication
- **Add**: Combine values
- **Lerp**: Linear interpolation
- **Time**: Animated effects
- **Normal From Texture**: Normal mapping
- **Fresnel Effect**: Edge lighting
- **Custom Function**: HLSL code

### Material Variants
- Use Sub Graphs for reusable logic
- Create material property overrides
- Use keywords for feature toggles

## Transparency Setup

```hlsl
// In Properties
[Enum(UnityEngine.Rendering.BlendMode)] _SrcBlend("Src Blend", Float) = 5 // SrcAlpha
[Enum(UnityEngine.Rendering.BlendMode)] _DstBlend("Dst Blend", Float) = 10 // OneMinusSrcAlpha
_ZWrite("Z Write", Float) = 0

// In SubShader Tags
Tags { "Queue" = "Transparent" "RenderType" = "Transparent" }

// In Pass
Blend [_SrcBlend] [_DstBlend]
ZWrite [_ZWrite]
```

## Best Practices

### Organization
- Use `HaroFramework/Category/ShaderName` naming
- Group related properties with headers
- Add tooltips for properties
- Include fallback shader

### Performance
- Minimize texture samples (max 4-8)
- Use LOD (Level of Detail) variants
- Profile with Frame Debugger
- Use GPU Instancing when possible

### URP Compatibility
- Use URP shader templates
- Include proper multi_compile pragmas
- Support main light and additional lights
- Implement ShadowCaster pass

### Version Control
- Shader Graph assets are text-based (YAML)
- Easy to merge and diff
- Include .meta files

## File Organization

```
Assets/
  Art/
    Shaders/
      ShaderGraphs/
        *.shadergraph
      CustomShaders/
        *.shader
      SubGraphs/
        *.shadersubgraph
    Materials/
      *.mat
```

## Questions to Ask

Before creating a shader:
1. What visual effect is needed?
2. Shader Graph or custom HLSL?
3. Lit or unlit?
4. Transparent or opaque?
5. Performance requirements?
6. Target platforms?

## Output Format

1. Create .shadergraph or .shader file in appropriate location
2. Include complete, working shader code
3. Add property descriptions and tooltips
4. Include usage instructions
5. Provide material setup guidance
6. Note performance considerations
