#%%
import numpy as np
import matplotlib.pyplot as plt
h1=0.1
h2=0.01
x=np.linspace(1,2,num=100)
df=1/x
df_f=(np.log(x+h1)-np.log(x))/h1
df_b=(np.log(x)-np.log(x-h1))/h1
df_c=(np.log(x+h1)-np.log(x-h1))/(2*h1)
#print(df)
err_f=np.abs(df-df_f)
err_b=np.abs(df-df_b)
err_c=np.abs(df-df_c)
# parint(err_f)

fig1=plt.figure(1)
plt.grid(color='lightgray')
plt.title('APPROXIMATION WITH h=0.1')
plt.plot(x,df,'-',color='crimson',label='df')
plt.plot(x,df_f,':',color='chocolate',label='df_c')
plt.plot(x,df_b,'-.',color='blueviolet',label='df_b')
plt.plot(x,df_c,'--',color='olivedrab',label='df_c')
plt.legend()
fig1.show()

fig2=plt.figure(2)
plt.grid(color='lightgray')
plt.title('Error WITH h=0.1')
plt.plot(x,err_f,':',color='chocolate',label='df_c')
plt.plot(x,err_b,'-.',color='blueviolet',label='df_b')
plt.plot(x,err_c,'--',color='olivedrab',label='df_c')
plt.legend()
fig2.show()

df_f=(np.log(x+h2)-np.log(x))/h2
df_b=(np.log(x)-np.log(x-h2))/h2
df_c=(np.log(x+h2)-np.log(x-h2))/(2*h2)

err_f=np.abs(df-df_f)
err_b=np.abs(df-df_b)
err_c=np.abs(df-df_c)

fig3=plt.figure(3)
plt.grid(color='lightgray')
plt.title('APPROXIMATION WITH h=0.01')
plt.plot(x,df,'-',color='crimson',label='df')
plt.plot(x,df_f,':',color='chocolate',label='df_c')
plt.plot(x,df_b,'-.',color='blueviolet',label='df_b')
plt.plot(x,df_c,'--',color='olivedrab',label='df_c')
plt.legend()
fig3.show

fig4=plt.figure(4)
plt.grid(color='lightgray')
plt.title('Error WITH h=0.01')
plt.plot(x,err_f,':',color='chocolate',label='df_c')
plt.plot(x,err_b,'-.',color='blueviolet',label='df_b')
plt.plot(x,err_c,'--',color='olivedrab',label='df_c')
plt.legend()
fig4.show()
# %%
