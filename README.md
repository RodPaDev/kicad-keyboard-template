# Kicad Mechanical Keyboard Template


This is a template project _(without actually being a KiCad template)_, it aims to facilitate the repetitiveness of starting a new mechanical keyboard project from scratch.

It already has the following libraries added

 - [MX_Alps_Hybrid by ai03](https://github.com/ai03-2725/MX_Alps_Hybrid)
 - [random-keyboard-parts by ai03](https://github.com/ai03-2725/random-keyboard-parts.pretty)


----

## Get Started

You need to install [Git](https://git-scm.com/) for the next step.

1. Clone this project and the submodules

```
git clone git@github.com:RodPaDev/kicad-keyboard-template.git <PROJECT_NAME>
or
git clone https://github.com/RodPaDev/kicad-keyboard-template.git <PROJECT_NAME>

cd <PROJECT_NAME>

git submodules init
git submodules update
```

2. Rename files:

If you don't have python installed, just do it manually.

**Automatic:**
```
python rename.py <YOUR_PROJECT_NAME>

If you make a typo you'll have to change the preifx variable to the current name (the one you entered)
```

**Manual:**

Rename the following files:
```
Keyboard_Template.kicad_pcb
Keyboard_Template.pro
Keyboard_Template.sch

```

## Notes:

This does not have anything done yet, the implementation is up to you. However, I may add branches in the future with some of the more "generic" parts already implemented and ready to use.



