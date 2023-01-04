const scan = (e,form) => {
    e.preventDefault();
    $("#prediction").html(`<div></div>`);
    $("#value").html(`<div></div>`);
    $("#table_name").css('display', 'none');
    const file = $("#image")[0].files[0];
    let fd = new FormData();
    fd.append("image",file);
    
    $("#display-img").html(`
        <center><div class="spinner-border" role="status">
            <span class="visually-hidden">Loading...</span>
        </div>
        <h5>Getting your prediction, please wait...</h5></center>
    `);

    fetch("/scan",{
        method:"Post",
        body:fd,
    })
        .then(async(res) => {
            const data = await res.json();

            $("#display-img").html(`
                <center><img src=${data.filepath} style="max-width:500px;max-height:500px;" /></center>
            `);
            if(data.prediction != ''){
                $("#prediction").html(`
                    <center><img src=${data.prediction} style="max-width:500px;max-height:500px;" /></center>
                `);
            }
            $("#value").html(`
                <h3><center>VIN Number: ${data.value}</center></h3>
            `);
        });
}

const detect = (e,form) => {
    e.preventDefault();
    $("#prediction").html(`<div></div>`);
    $("#value").html(`<div></div>`);
    $("#table_name").css('display', 'none');
    const file = $("#image")[0].files[0];
    let fd = new FormData();
    fd.append("image",file);
    
    $("#display-img").html(`
        <center><div class="spinner-border" role="status">
            <span class="visually-hidden">Loading...</span>
        </div>
        <h5>Getting your prediction, please wait...</h5></center>
    `);

    fetch("/detect",{
        method:"Post",
        body:fd,
    })
        .then(async(res) => {
            const data = await res.json();

            $("#display-img").html(`
                <center><img src=${data.filepath} style="max-width:500px;max-height:500px;" /></center>
            `);
            if(data.prediction != ''){
                $("#prediction").html(`
                    <center><img src=${data.prediction} style="max-width:500px;max-height:500px;" /></center>
                `);
            }
            $("#value").html(`
                <h3><center>VIN Number: ${data.value}</center></h3>
            `);
        });
}