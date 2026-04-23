import os

file_path = r"c:\Users\ok\Downloads\pawbehavior (1)\src\App.tsx"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace common input class pattern
content = content.replace(
    'className="w-full px-4 py-3 rounded-xl border border-zinc-800 focus:ring-2 focus:ring-gold-500 outline-none"',
    'className="w-full px-4 py-3 rounded-xl border border-zinc-800 bg-zinc-950 text-zinc-100 placeholder-zinc-600 focus:ring-2 focus:ring-gold-500 outline-none"'
)

# Also fix the login error box to be dark mode compatible
content = content.replace(
    'className="p-4 rounded-2xl bg-red-50 text-red-600 text-sm space-y-2"',
    'className="p-4 rounded-2xl bg-red-500/10 border border-red-500/20 text-red-400 text-sm space-y-2"'
)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Input styling fix complete.")
