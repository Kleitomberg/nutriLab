    paciente = document.querySelector('#paciente_id')
   

    fetch("/grafico_peso/"+paciente.value+"/",{
        method: 'POST',
    }).then(function(result){
        return result.json()
    }).then(function(data_paciente){
       
        const data = {
            labels: data_paciente['labels'],
            datasets: [{
            label: 'Peso paciente',
            backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(255, 99, 132)',
            data: data_paciente['peso'],
            }]
        };

        const config = {
            type: 'line',
            data: data,
            options: {}
        };

        const myChart = new Chart(
            document.getElementById('myChart'),
            config
        );


    })



