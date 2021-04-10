var intervalID;
var beerTimerID;
var confettiTimerID;

function updateCurrentTime(){
    var input = $("#currentDate").html();
    if (input){
        input = input.replace('.', '');
        var dateFrom = new Date(input);
        var now = new Date();
        var duration = (now.getTime() - dateFrom.getTime()) / 1000 - 60*60;
        var hours = parseInt(duration / 60 / 60);
        var minutes = parseInt(duration / 60) - hours*60;
        var seconds = parseInt(duration - minutes*60 - hours*60*60);
        var result = "";
        if (hours > 0){
            result += hours + " Hours "
        }
        if (minutes > 0){
            result += minutes + " Minutes "
        }
        result += seconds + " Seconds"
        $("#lastDiff").html(result);
    }
}

intervalID = setInterval(updateCurrentTime,1000);
if (! $("#currentDate").html()){
    clearInterval(intervalID);
}

async function fetchUpdates(){
    let response = await fetch("/beer/update");

    if (response.status == 200) {
        return response.json();
    }
}

async function doPoll(once=false){
    const response = await fetchUpdates();

    render(response);

    if (!once){
        if (Number($("#totalbeer").attr('total')) < 150){
            setTimeout(function(){
                    doPoll();
                }, 2000);
        }
    }

}

function render(data){
    if (data["lastCount"] > $("#crate").attr('count')){
        $("#crate").attr('count', data["lastCount"]);
        $("#crate").html('');
        $("#crates").html('');
        var crates = Math.ceil(Number(data["lastCount"]) / 20) - 1;
        var bottles = Number(data["lastCount"]) % 20;
        var total = Number(data["lastCount"]);
        $("#totalbeer").attr('total', total);

        if (bottles == 0){
            crates += 1;
        }

        $(".crate-count").each(function(elem){
            $(this).html(crates);
        });
        $(".beer-count").html(total);
        for (var i = 0; i < bottles; i++){
                $("#crate").append('<div><img src="/static/sterni.png" alt="Sterni" style="width: 70px;"></div>');
            }
        for (var i = 0; i < crates; i++){
            $("#crates").append('<div><img src="/static/sterni_kasten.edit.png" alt="Sterni Kasten" style="width: 150px;"></div>');
        }
        $("#currentDate").html(data["time"]);
        $("#info").html("Total: " + total + " Bottles or <strong>" + total * 1.0 + " Euro (1,00/Bottle)");
        $("#destination1").html((total / 2.0).toFixed(2) + " Euro");
        $("#destination2").html((total / 2.0).toFixed(2) + " Euro");

        if (total >= 150){
            $("#currentInfo").hide();
            $("#endInfo").show();
            $("#lastDiff").parent().hide();
            clearInterval(intervalID);
            $("#restartConfetti").click();
            $("#confettiCanvas").css('z-index', -99);
            $("#success_beer").show();
            $("#click_me").hide();
            $("#add").hide();
            $("#beer-content").insertAfter($("#fundraising-content"));
            clearTimeout(beerTimerID);
            clearTimeout(confettiTimerID);
        }
    }
}

$(function(){
    var context = new AudioContext();
    $("#add").on("click", function(event){
        var init = false;
        if ($("#lastLocalUpdate").html() == ""){
            $("#lastLocalUpdate").html(new Date());
            console.log("init")
            init = true;
        }
        var lastLocalUpdate = new Date($("#lastLocalUpdate").html());

        if ((new Date()).getTime() - lastLocalUpdate.getTime() > 60*1000 || init){
            $("#lastLocalUpdate").html(new Date());

            $("#restartConfetti").click();
            $("#success_beer").show();

            beerTimerID = setTimeout(function(){
                $("#stopConfetti").click();
            }, 8000);

            confettiTimerID = setTimeout(function(){
                $("#success_beer").hide();
            }, 11000);
            $('audio#pop')[0].play();

            $.get('/beer/add', function(data){
                doPoll(true);
            });
        }
        else{
            $("#tooFast").show();
            console.log("not log enough...");
            console.log((new Date()).getTime() - lastLocalUpdate.getTime());
        }
    });

    doPoll();
})