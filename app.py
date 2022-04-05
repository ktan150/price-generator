#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask


# In[2]:


app = Flask(__name__)


# In[3]:


from flask import request, render_template
import joblib 

@app.route("/", methods=["GET", "POST"]) 
def index():
    if request.method == "POST":
        latitude = request.form.get("latitude")
        longitude = request.form.get("longitude")
        microwave = request.form.get("microwave")
        smoking_allowed = request.form.get("smoking_allowed")
        p_livingroom = request.form.get("p_livingroom")
        print(longitude, latitude, microwave,smoking_allowed,p_livingroom)
        model = joblib.load("Automatic_Price_Generator")
        pred = model.predict([[float(latitude), float(longitude),int(microwave),int(smoking_allowed),int(p_livingroom)]])
        print(pred)
        pred = pred[0]
        s = "The predicted price for your apartment is $" + str(pred)
        return(render_template("index.html", result=s))
    else: 
        return(render_template("index.html", result="Please enter the required information to estimate a price to charge your guests"))


# In[ ]:


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int("80"))


# In[ ]:




