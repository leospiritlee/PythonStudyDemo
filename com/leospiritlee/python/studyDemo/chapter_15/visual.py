import pygal

class Visual():

    def __init__(self, x_title='x_title', y_title = 'y_title',title = 'title',result = [], pic_name = 'default.svg'):
        self.x_title = x_title
        self.y_title = y_title
        self.result = result
        self.title = title
        self.pic_name = pic_name

    def draw(self):
        hist = pygal.Bar()

        hist.title =  self.title


        hist.x_title = self.x_title
        hist.y_title = self.y_title

        hist.add('', self.result)
        hist.render_to_file(self.pic_name)