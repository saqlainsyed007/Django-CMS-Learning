$(document).ready(function(){
	$('.dnn-agree-disagree-yes').click(function(){
		$(this).find('g g').attr("stroke", "white");
		$(this).find('g g').attr("fill", "#00436C");
		$(this).find('.dnn-agree-disagree-caption').addClass('dnn-agree-disagree-caption-selected');
		$(this).siblings('.dnn-agree-disagree-no').find('.dnn-agree-disagree-caption').removeClass('dnn-agree-disagree-caption-selected');
		$(this).siblings('.dnn-agree-disagree-no').find('g g').attr("fill", "white");
		$(this).siblings('.dnn-agree-disagree-no').find('g g').attr("stroke", "#0079C1");
		var id = $(this).attr('pluginInstance');
		$.ajax({
           url: "/agreeDisagree/updateSelection/"+id+"/1",
           data: {},
           type: "GET",
       });
	});
	$('.dnn-agree-disagree-no').click(function(){
		$(this).find('g g').attr("stroke", "white");
		$(this).find('g g').attr("fill", "#00436C");
		$(this).find('.dnn-agree-disagree-caption').addClass('dnn-agree-disagree-caption-selected');
		$(this).siblings('.dnn-agree-disagree-yes').find('.dnn-agree-disagree-caption').removeClass('dnn-agree-disagree-caption-selected');
		$(this).siblings('.dnn-agree-disagree-yes').find('g g').attr("fill", "white");
		$(this).siblings('.dnn-agree-disagree-yes').find('g g').attr("stroke", "#0079C1");
		var id = $(this).attr('pluginInstance');
		$.ajax({
           url: "/agreeDisagree/updateSelection/"+id+"/0",
           data: {},
           type: "GET",
       });
	});
})