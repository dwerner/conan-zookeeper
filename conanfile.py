from conans import ConanFile
import os
from conans.tools import download
from conans.tools import unzip
from conans import CMake

class zookeeperConan(ConanFile):
    name = "zookeeper"
    version = "0.13.3"
    generators = "cmake"
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    url="http://github.com/dwerner/conan-zookeeper"
    license="https://github.com/google/googletest/blob/master/googletest/LICENSE"
    exports="FindZookeeper.cmake"
    unzipped_name = "zookeeper-%s" % version
    zip_name = "%s.zip" % unzipped_name

    def source(self):
        url = "https://apache.mirror.gtcomm.net/zookeeper/%s/%s" % (self.unzipped_name, self.zip_name)  
        download(url, self.zip_name)
        unzip(self.zip_name)
        os.unlink(self.zip_name)

    def build(self):
        cd_build = "cd %s" % self.unzipped_name
        self.run("%s && make" % cd_build)

    def package(self):
        # Copy findzookeeper script into project
        self.copy("FindZookeeper.cmake", ".", ".")

        # Copying headers
        self.copy(pattern="*.h", dst="include", src="./include", keep_path=False)

        # Copying static and dynamic libs
        self.copy(pattern="*.a", dst="lib", src=".libs/", keep_path=False)
        self.copy(pattern="*.lib", dst="lib", src=".libs/", keep_path=False)
        self.copy(pattern="*.dll", dst="bin", src=".libs/", keep_path=False)
        self.copy(pattern="*.so*", dst="lib", src=".libs/", keep_path=False)
        self.copy(pattern="*.dylib*", dst="lib", src=".libs/", keep_path=False)      

    def package_info(self):
        self.cpp_info.libs = ['zookeeper']
