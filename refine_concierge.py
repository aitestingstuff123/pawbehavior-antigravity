import os

file_path = r"c:\Users\ok\Downloads\pawbehavior (1)\src\App.tsx"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Fix login screen background
content = content.replace(
    'className="min-h-screen bg-gradient-to-br from-indigo-50 via-white to-purple-50 flex flex-col items-center justify-center p-4"',
    'className="min-h-screen bg-zinc-950 flex flex-col items-center justify-center p-4 relative overflow-hidden"'
)

# 2. Add some luxury decorative elements to login screen (subtle gold glows)
# Find the login container and add an ambient glow
login_container = '<motion.div \n            initial={{ opacity: 0, y: 20 }}\n            animate={{ opacity: 1, y: 0 }}\n            className="bg-zinc-900 p-8 rounded-[2rem] shadow-2xl w-full max-w-md border border-zinc-800 relative z-10"'
new_login_container = '''
          {/* Subtle ambient glows */}
          <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[800px] h-[800px] bg-gold-500/5 rounded-full blur-[120px] pointer-events-none" />
          <motion.div 
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className="bg-zinc-900/80 backdrop-blur-xl p-8 rounded-[2rem] shadow-[0_0_40px_rgba(212,175,55,0.05)] w-full max-w-md border border-zinc-800/50 relative z-10"'''

content = content.replace(login_container, new_login_container)

# 3. Concierge Terminology and Typography
content = content.replace(
    '<h1 className="text-4xl font-bold tracking-tight text-zinc-100">PawBehavior</h1>',
    '<h1 className="text-4xl font-black font-serif tracking-tight text-gold-400">PawBehavior</h1>\n            <p className="text-[10px] tracking-[0.3em] uppercase text-gold-600 mt-2 font-bold">Premium Concierge</p>'
)

content = content.replace(
    '<span className="font-bold font-serif text-lg text-zinc-100">PawBehavior</span>',
    '''<div className="flex flex-col">
              <span className="font-black font-serif text-xl text-gold-400 leading-none">PawBehavior</span>
              <span className="text-[8px] tracking-[0.2em] uppercase text-gold-600 font-bold">Concierge</span>
            </div>'''
)

content = content.replace(
    '<span className="font-bold text-xl text-zinc-100">PawBehavior</span>',
    '''<div className="flex flex-col">
              <span className="font-black font-serif text-2xl text-gold-400 leading-none">PawBehavior</span>
              <span className="text-[9px] tracking-[0.2em] uppercase text-gold-600 font-bold mt-1">Premium Concierge</span>
            </div>'''
)

content = content.replace(
    '<h3 className="text-2xl font-black text-zinc-100 mb-3">\n          Unlock PawBehavior Pro\n        </h3>',
    '<h3 className="text-2xl font-black font-serif text-gold-400 mb-3">\n          Unlock Premium Concierge\n        </h3>'
)

# 4. Small luxury tracker text mimicking the mockup
# Find the main dashboard header and add it above
main_header_search = '<h2 className="text-2xl lg:text-3xl font-black text-zinc-100">'
main_header_replace = '<p className="text-[10px] tracking-[0.2em] uppercase text-gold-600/70 font-bold mb-2">System Status / Optimized</p>\n          <h2 className="text-2xl lg:text-3xl font-black font-serif text-zinc-100">'
content = content.replace(main_header_search, main_header_replace)

# Apply gold color to streak icon container
content = content.replace(
    'className={`w-6 h-6 lg:w-8 lg:h-8 ${hasUploadedToday ? \'text-gold-500\' : \'text-zinc-300\'}`}',
    'className={`w-6 h-6 lg:w-8 lg:h-8 ${hasUploadedToday ? \'text-gold-400 drop-shadow-[0_0_8px_rgba(212,175,55,0.5)]\' : \'text-zinc-600\'}`}'
)

# Change pet card names to serif
content = content.replace(
    '<h3 className="font-bold text-lg text-zinc-100">',
    '<h3 className="font-bold font-serif text-2xl text-zinc-100 tracking-wide">'
)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Concierge pass complete.")
