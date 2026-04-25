---
name: Serene Sand
colors:
  surface: '#fef8f4'
  surface-dim: '#dfd9d5'
  surface-bright: '#fef8f4'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f9f2ef'
  surface-container: '#f3ede9'
  surface-container-high: '#ede7e3'
  surface-container-highest: '#e7e1de'
  on-surface: '#1d1b19'
  on-surface-variant: '#4d453e'
  inverse-surface: '#32302e'
  inverse-on-surface: '#f6f0ec'
  outline: '#7f756d'
  outline-variant: '#d0c5ba'
  surface-tint: '#6b5c4a'
  primary: '#6b5c4a'
  on-primary: '#ffffff'
  primary-container: '#dcc7b1'
  on-primary-container: '#625241'
  inverse-primary: '#d8c3ad'
  secondary: '#665d54'
  on-secondary: '#ffffff'
  secondary-container: '#eee0d4'
  on-secondary-container: '#6c6359'
  tertiary: '#625e56'
  on-tertiary: '#ffffff'
  tertiary-container: '#d0cac0'
  on-tertiary-container: '#59554d'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#f5dfc8'
  primary-fixed-dim: '#d8c3ad'
  on-primary-fixed: '#241a0c'
  on-primary-fixed-variant: '#534434'
  secondary-fixed: '#eee0d4'
  secondary-fixed-dim: '#d1c4b9'
  on-secondary-fixed: '#211a13'
  on-secondary-fixed-variant: '#4e453d'
  tertiary-fixed: '#e8e2d8'
  tertiary-fixed-dim: '#ccc6bc'
  on-tertiary-fixed: '#1e1b15'
  on-tertiary-fixed-variant: '#4a463f'
  background: '#fef8f4'
  on-background: '#1d1b19'
  surface-variant: '#e7e1de'
typography:
  headline-xl:
    fontFamily: Newsreader
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Newsreader
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Newsreader
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.7'
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 13px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  container-max: 1120px
  gutter: 20px
---

## Brand & Style

This design system is built upon the principles of **Minimalism** with a tactile, organic influence. It seeks to evoke a sense of calm, intellectual clarity, and warmth, moving away from the sterile whites of traditional minimalism toward a more "lived-in" and editorial feel. 

The target audience is composed of thoughtful readers and creators who value focus and long-form content. The UI stays out of the way, acting as a sophisticated frame for imagery and text. The emotional response is one of tranquility and reliability, achieved through a restricted color palette and generous negative space.

## Colors

The palette is rooted in earth tones. The primary color is a warm sand that serves as the main interactive accent. The background is a slightly desaturated off-beige to reduce eye strain compared to pure white. 

- **Primary**: Warm Sand (#DCC7B1) used for key call-to-actions and active states.
- **Secondary**: Muted Umber (#5C534A) for subheadings and secondary icons.
- **Tertiary**: Pale Bone (#EAE3D9) used for subtle surface layering.
- **Neutral**: Deep Charcoal (#211F1D) for maximum readability in body text.

## Typography

This design system employs a sophisticated pairing of a serif and a geometric sans-serif. 

**Newsreader** is used for headlines to provide a literary, editorial feel that establishes authority. **Plus Jakarta Sans** is used for body copy and UI labels; its soft curves complement the rounded UI elements while maintaining high legibility at small sizes. All body text should maintain a generous line height to ensure a breezy, comfortable reading experience.

## Layout & Spacing

The layout follows a **Fixed Grid** model for desktop, transitioning to a fluid single-column for mobile. The system uses an 8px base unit to maintain a consistent rhythm.

On desktop, content is centered within a 1120px container. For the "blog board" view, a masonry or justified grid should be used with a 24px (md) gap between cards. Margins on mobile are set to 20px to provide a breathable frame for content.

## Elevation & Depth

Depth is achieved through **Ambient Shadows** and **Tonal Layers** rather than heavy borders. 

Surfaces use extremely soft, diffused shadows with a slight warm tint (#5C534A at 8% opacity) to make cards feel like they are gently resting on the sand-colored background. We use "Layered Tones" where the background is the darkest "warm" shade, and cards are the lightest (off-white/cream), creating a natural lift. Avoid harsh black shadows; elevation should feel like natural sunlight.

## Shapes

The shape language is defined by **Rounded** corners, which reinforce the approachable and soft aesthetic. 

Standard components (buttons, input fields) use a 0.5rem (8px) radius. Larger containers like blog cards and image wrappers use `rounded-xl` (1.5rem/24px) to create a distinct, friendly silhouette. This consistency in rounding helps unify different content types (text posts vs. images).

## Components

- **Buttons**: Primary buttons are solid Sand (#DCC7B1) with Dark Charcoal text. Secondary buttons use a ghost style with a subtle 1px border in Umber.
- **Cards**: Blog cards feature a "Cream" background, `rounded-xl` corners, and the signature ambient shadow. On hover, cards should lift slightly (shadow expansion) to provide tactile feedback.
- **Chips/Tags**: Small, pill-shaped elements using the Tertiary color (#EAE3D9) with `label-sm` typography. 
- **Input Fields**: Soft beige backgrounds with no border, only a 2px bottom stroke that darkens on focus.
- **Progress Indicators**: Thin, elegant lines using the primary Sand color.
- **Navigation**: A minimal top bar with high transparency and a background blur (Glassmorphism) to keep the focus on the content as the user scrolls.