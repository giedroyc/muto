from sanic import Sanic

from sanic.response import json, html

app = Sanic()

@app.route("/")
async def test(request):
    return json({"hello": "world"})

@app.route("/data")
async def data(request):
    import datasources.data
    return html(datasources.data.data.compute().to_html())

@app.route("/data/<i:int>")
async def data(request, i):
    import datasources.data
    df = datasources.data.data.compute()
    return json(df.loc[i].to_json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)