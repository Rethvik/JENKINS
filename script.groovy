def greetUser(){
    echo "Hi ${NAME}"
}
def suggestUser(){
    if(params.age.toInteger()>13){
        echo 'You are in youthful age'
    }else{
        echo 'You are teenager'
    }
}
return this