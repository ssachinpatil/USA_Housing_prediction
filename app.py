from Model.utils import housing
from flask import Flask,request,render_template

app=Flask(__name__)
@app.route('/')
def result():
    return render_template ('index.html')

@app.route('/output',methods=['POST'])
def ans():
    input=request.form.get
    Avg_AreaIncome=float(input('Avg_AreaIncome'))
    Avg_AreaHouseAge=float(input('Avg_AreaHouseAge'))
    Avg_AreaNumberofRooms =float(input('Avg_AreaNumberofRooms'))
    Avg_AreaNumberofBedrooms=float(input('Avg_AreaNumberofBedrooms'))
    AreaPopulation=float(input('AreaPopulation'))

    obj=housing(Avg_AreaIncome,Avg_AreaHouseAge,Avg_AreaNumberofRooms,Avg_AreaNumberofBedrooms,AreaPopulation)
    pred=obj.prediction()
    return render_template ('index.html',res=pred)
if __name__=="__main__":
    app.run(host='0.0.0.0',port=9099)