import generateJoke from "./generateJoke";
import './styles/main.scss'
import laughing from './assets/laughing.svg'
import getFunction from "./getfunction";
import addEmployeeRestApi from "./addFunction";

const laughImg = document.getElementById('laughImg')
laughImg.src = laughing;

const jokeBtn = document.getElementById('jokeBtn')
jokeBtn.addEventListener('click', generateJoke) 
jokeBtn.addEventListener('click',addEmployeeRestApi)
jokeBtn.addEventListener('click',getFunction('2'))

generateJoke()

console.log(generateJoke())

fetch("https://j5igw9ry82.execute-api.eu-north-1.amazonaws.com/test")
.then(response => response.text())
.then(data => console.log(data))

.catch(error =>{
    console.log(error);
});
