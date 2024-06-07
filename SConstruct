#!/usr/bin/env python

libname = 'data_manager'
env = SConscript('godot-cpp/SConstruct')
env.Append(CPPPATH=['src'])

src = Glob('src/*.cpp')
libpath = 'bin/lib_{}{}{}'.format(libname, env['suffix'], env['SHLIBSUFFIX'])
sharedlib = env.SharedLibrary(libpath, src)
Default(sharedlib)

