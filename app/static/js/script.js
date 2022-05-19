$(document).ready(function(){
    $("#quiz").submit(function(event){
      event.preventDefault();
      $(".results").hide();
  
      var home=$("input:radio[name=home]:checked").val();
      var play=$("input:radio[name=play]:checked").val();
      var space=$("input:radio[name=space]:checked").val();
      var noise=$("input:radio[name=noise]:checked").val();
      var activity=$("input:radio[name=activity]:checked").val();
  //parrot,fish,dog,cat,rabbit
      if (!home || !play || !space || !noise || !activity) {
        alert("Please answer the questions.")
      } else if (play === "often" && space != "small" && noise != "low" && activity != "low") {
        $("#dog").show();
      } else if (noise === "low" && play === "rarely" || home === "rarely" && activity === "low") {
        $("#rabbit").show();
      } else if (noise !== "low" && play === "rarely" && home === "rarely" && activity === "low" && space == "small") {
        $("#parrot").show();
      } else if (noise === "low" && play === "rarely" || space === "small"|| home === "rarely" && activity === "low"){
        $("#fish").show();
      } else {
        $("#cat").show(); 
      }
  
    });
  });
  // $(document).ready(function() {
  //   $("#reset").click(function() {
  //       $('#myform').find('input, select').not(':button, :submit, :reset, :hidden').val('').removeAttr('checked').removeAttr('selected');
  //   });
  // });

