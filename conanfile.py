from conans import ConanFile
import os
from conans.tools import download
from conans.tools import unzip
from conans import CMake

class zookeeperConan(ConanFile):
    name = "zookeeper"
    version = "3.4.8"
    generators = "cmake"
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    url="http://github.com/dwerner/conan-zookeeper"
    license="https://www.apache.org/licenses/LICENSE-2.0"
    exports="FindZookeeper.cmake"
    unzipped_name = "zookeeper-%s" % version
    zip_name = "%s.tar.gz" % unzipped_name

    def source(self):
        url = "http://apache.mirror.rafal.ca/zookeeper/%s/%s" % (self.unzipped_name, self.zip_name)  
        download(url, self.zip_name)
        unzip(self.zip_name)
        os.unlink(self.zip_name)

    def build(self):
        self.run("cd %s/src/c && ./configure && make" % self.unzipped_name)

    def package(self):
        # Copy findzookeeper script into project
        self.copy("FindZookeeper.cmake", ".", ".")

        # Copying headers
        self.copy(pattern="*.h", dst="include/zookeeper", src="%s/src/c/include" % self.unzipped_name, keep_path=False)

        libdir = "%s/src/c/.libs/" % self.unzipped_name
        # Copying static and dynamic libs
        self.copy(pattern="*.a", dst="lib", src=libdir, keep_path=False)
        self.copy(pattern="*.lib", dst="lib", src=libdir, keep_path=False)
        self.copy(pattern="*.so*", dst="lib", src=libdir, keep_path=False)
        self.copy(pattern="*.dylib*", dst="lib", src=libdir, keep_path=False)      
        self.copy(pattern="*.dll", dst="bin", src=libdir, keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ['zookeeper']
