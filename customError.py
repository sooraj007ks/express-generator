class Errors(object):
    def reportError(self, when, error):
        title = 'Error'
        print title
        print '-' * len(title)
        print 'Error occurred while {}.\nDetails - {}'.format(when, error)