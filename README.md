[![Build Status](https://travis-ci.org/dwerner/conan-hiredis.svg)](https://travis-ci.org/dwerner/conan-hiredis)


# conan-hiredis

[Conan.io](https://conan.io) package for hiredis library

## Build packages

Download conan client from [Conan.io](https://conan.io) and run:

    $ python build.py
    
## Upload packages to server

    $ conan upload hiredis/0.13.3@dwerner/stable --all
    
## Reuse the packages

### Basic setup

    $ conan install hiredis/0.13.3@dwerner/stable
    
### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*
    
    [requires]
    hiredis/0.13.3@dwerner/testing

    [options]
    hiredis:shared=true # false
    
    [generators]
    txt
    cmake

Complete the installation of requirements for your project running:</small></span>

    conan install . 

Project setup installs the library (and all his dependencies) and generates the files *conanbuildinfo.txt* and *conanbuildinfo.cmake* with all the paths and variables that you need to link with your dependencies.
