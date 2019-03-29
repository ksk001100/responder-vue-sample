import responder

api = responder.API()

if __name__ == '__main__':
    api.add_route('/', static=True)
    api.run()
