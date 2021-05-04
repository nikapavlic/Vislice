import bottle
import model

#treba pisat model.Vislice() drugače neve od kod je
vislice = model.Vislice()


@bottle.get('/')
def index():
    return bottle.template('index.tpl')

bottle.run(reloader = True, debug = True)