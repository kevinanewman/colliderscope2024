if __name__ == "__main__":
    import os, sys, subprocess
    import traceback

    try:
        path = os.path.dirname(os.path.abspath(__file__))

        uic_ommand = '%s -p' % sys.executable.replace('python', 'pyside6-uic')

        package_folder = '%s' % path

        subpackage_list = [package_folder + os.sep + d for d in os.listdir(package_folder)
                           if os.path.isdir(package_folder + os.sep + d)
                           and '__init__.py' in os.listdir('%s%s%s' % (package_folder, os.sep, d))]

        subpackage_list.append(package_folder)

        for source_folder in subpackage_list:
            source_files = [fn for fn in os.listdir(source_folder) if '.ui' in fn]
            for f in source_files:

                cmd_str = '%s %s -o %s' % (uic_ommand, os.path.join(source_folder, f), source_folder + os.sep + 'ui_%s.py' % f.replace('.ui', ''))

                print('Trying %s' % cmd_str)

                r = os.system(cmd_str)
    except:
        pass
