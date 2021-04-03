// var name_btn = document.getElementsBId("name_btn");

// function handleClick(event) {
//     console.log(event.target);
//     console.log(event.target.IdList);

//     if (event.target.IdList[1] === "clicked") {
//         event.target.IdList.remove("clicked");
//     } else {
//         for (var i = 0; i < name_btn.length; i++) {
//             name_btn[i].IdList.remove("clicked");
//         }
//         event.target.IdList.add("clicked");
//     }
// }

// var name_btn = document.getElementById("name_btn");
// name_btn.addEventListener('click', function){

// }



function view(btn_value) {
    if (btn_value == "곽민아") {
        document.ma_hide_and_show_form.name_btn.value = "곽 민 아";
        document.getElementById('ma_display_btn').style.display = 'block';
    } else if (btn_value == "곽 민 아") {
        document.ma_hide_and_show_form.name_btn.value = "곽민아";
        document.getElementById('ma_display_btn').style.display = 'none';
    }
    else if (btn_value == "김예빈") {
        document.yb_hide_and_show_form.name_btn.value = "김 예 빈";
        document.getElementById('yb_display_btn').style.display = 'block';

    } else if (btn_value == "김 예 빈") {
        document.yb_hide_and_show_form.name_btn.value = "김예빈";
        document.getElementById('yb_display_btn').style.display = 'none';
    }
    else if (btn_value == "박성제") {
        document.sj_hide_and_show_form.name_btn.value = "박 성 제";
        document.getElementById('sj_display_btn').style.display = 'block';

    } else if (btn_value == "박 성 제") {
        document.sj_hide_and_show_form.name_btn.value = "박성제";
        document.getElementById('sj_display_btn').style.display = 'none';
    }
    else if (btn_value == "이서현") {
        document.sh_hide_and_show_form.name_btn.value = "이 서 현";
        document.getElementById('sh_display_btn').style.display = 'block';

    } else if (btn_value == "이 서 현") {
        document.sh_hide_and_show_form.name_btn.value = "이서현";
        document.getElementById('sh_display_btn').style.display = 'none';
    }
    else if (btn_value == "한준혁") {
        document.jh_hide_and_show_form.name_btn.value = "한 준 혁";
        document.getElementById('jh_display_btn').style.display = 'block';

    } else if (btn_value == "한 준 혁") {
        document.jh_hide_and_show_form.name_btn.value = "한준혁";
        document.getElementById('jh_display_btn').style.display = 'none';
    }
};
