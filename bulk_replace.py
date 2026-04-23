import os

file_path = r"c:\Users\ok\Downloads\pawbehavior (1)\src\App.tsx"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

replacements = {
    # Backgrounds
    "bg-slate-50": "bg-zinc-950",
    "bg-white": "bg-zinc-900",
    "bg-slate-100": "bg-zinc-800",
    "hover:bg-slate-50": "hover:bg-zinc-800",
    "hover:bg-slate-100": "hover:bg-zinc-800",
    "hover:bg-slate-200": "hover:bg-zinc-700",
    "bg-indigo-50": "bg-gold-500/10",
    "bg-indigo-100": "bg-gold-500/20",
    "bg-indigo-600": "bg-gold-500",
    "hover:bg-indigo-700": "hover:bg-gold-600",
    "bg-amber-50": "bg-zinc-800",
    "bg-amber-100": "bg-gold-500/20",
    "bg-emerald-50": "bg-zinc-800",
    "bg-emerald-100": "bg-emerald-500/20",
    "bg-rose-50": "bg-zinc-800",
    "bg-rose-100": "bg-rose-500/20",

    # Text Colors
    "text-slate-900": "text-zinc-100",
    "text-slate-800": "text-zinc-200",
    "text-slate-700": "text-zinc-300",
    "text-slate-600": "text-zinc-400",
    "text-slate-500": "text-zinc-400",
    "text-slate-400": "text-zinc-500",
    "text-indigo-600": "text-gold-400",
    "text-indigo-700": "text-gold-300",
    "hover:text-indigo-600": "hover:text-gold-300",
    "text-amber-600": "text-gold-400",
    "text-amber-500": "text-gold-500",
    
    # Borders
    "border-slate-200": "border-zinc-800",
    "border-slate-100": "border-zinc-800",
    "border-indigo-100": "border-gold-500/20",
    "border-indigo-600": "border-gold-500",
    "border-amber-200": "border-gold-500/50",
    "focus:border-indigo-500": "focus:border-gold-500",
    "focus:ring-indigo-500": "focus:ring-gold-500",

    # Shadows
    "shadow-sm": "shadow-[0_4px_20px_rgba(0,0,0,0.4)]",
    "shadow-md": "shadow-[0_8px_30px_rgba(0,0,0,0.5)]",
    "shadow-xl": "shadow-[0_10px_40px_rgba(0,0,0,0.6)]",
    "shadow-indigo-100": "shadow-gold-500/20",
}

for old, new in replacements.items():
    content = content.replace(old, new)

# Typography updates
content = content.replace('font-black text-zinc-100', 'font-black font-serif text-zinc-100')
content = content.replace('font-bold text-zinc-100', 'font-bold font-serif text-zinc-100')
content = content.replace('font-bold text-lg text-zinc-100', 'font-bold font-serif text-lg text-zinc-100')
content = content.replace('text-2xl font-bold', 'text-2xl font-bold font-serif')
content = content.replace('text-3xl font-black', 'text-3xl font-black font-serif')
content = content.replace('text-4xl font-black', 'text-4xl font-black font-serif')
content = content.replace('text-xl font-bold', 'text-xl font-bold font-serif')

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Replacement complete.")
