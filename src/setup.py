from setuptools import setup
import setup_translate

pkg = 'SystemPlugins.vps'
setup(name='enigma2-plugin-systemplugins-vps',
       version='3.0',
       description='VPS-Plugin',
       package_dir={pkg: 'vps'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo', 'LICENSE', 'maintainer.info', 'web/*.xml', 'web-data/*.html']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
