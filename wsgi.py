from app import app

if __name__ == '__main__':
    # debug = False
    debug = True
    port = 5000
    #clustering('2022-01-03 00:00:00' , 5)
    #print(df4.head())
    #show_agent_shedule()
    app.run(debug=debug, port=port)
