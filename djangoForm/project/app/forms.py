from django import forms
from .models import Student

class Registrationform(forms.ModelForm):
    # name = forms.CharField(max_length=50)
    # email = forms.EmailField()
    # contact = forms.IntegerField()
    # image = forms.ImageField()
    # resume = forms.FileField()
    class Meta:
        model = Student
        fields = '__all__'

    def clean(self):

        cleaned_data =  super().clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        contact = cleaned_data.get('contact')
        image = cleaned_data.get('image')
        resume = cleaned_data.get('resume')
        print(name)

        if not name:
            self.add_error('name',"plese enter your name")

        elif not name.replace(" ","").isalpha():
            self.add_error('name',"plese enter alpha")

        if not email:
            self.add_error('email',"plese enter email")

        elif not email.lower().endswith(("@gmail.com","@yahoo.com")):
             self.add_error('email'," plese only gmail and yaho")

        if not contact:
            self.add_error( 'contact' ,"plese enter contact")
        
        elif not len(str(contact)) == 10:
            self.add_error('contact',"plese only 10 digit number")

        if image:
            if image.size > 2 * 1024 * 1024:
                self.add_error('image',"image size should be less than 2 mb")

            elif not image.name.lower().endswith((".jpg",".png")):
                self.add_error('image',"only support jpg and png")
        else:
            self.add_error('image',"please uplod your image")

        if resume:
            if resume.size > 5 * 1024 * 1024:
                self.add_error()


            






# class Loginform(forms.Modelform):
#     class Meta:
#         model = Student
#         field = ['email','cintact']
        