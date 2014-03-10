var width = 990,
    height = 560,
    color = d3.scale.category20c();

var treemap = d3.layout.treemap()
    .size([width, height])
    .sticky(true)
    .value(function(d) { return d.size; });

var div = d3.select("#chart").append("div")
    .style("position", "relative")
    .style("width", width + "px")
    .style("height", height + "px");

d3.json("classesd3.json", function(json) {
        div.data([json]).selectAll("div")
      .data(treemap.nodes)
      .enter().append("div")
      .attr("class", "cell")
	    .style("font", "8pt Comic Sans MS")
      .style("background", function(d) { return  color(d.name); })
      .call(cell)
      .append("a")
      .attr("href", function(d) {return d.uri;}) 
      .text(function(d) { return  d.name + ":" + d.size; })
      
     
      
      //.text(function(d) { return d.children ? null : d.size; })
      
      
	 

  d3.select("#size").on("click", function() {
    div.selectAll("div")
        .data(treemap.value(function(d) { return d.size; }))
		
        .transition()
        .duration(1500)
        .call(cell);

    d3.select("#size").classed("active", true);
    d3.select("#count").classed("active", false);
  });

  d3.select("#count").on("click", function() {
    div.selectAll("div")
        .data(treemap.value(function(d) { return 1; }))
      .transition()
        .duration(1500)
        .call(cell);

    d3.select("#size").classed("active", false);
    d3.select("#count").classed("active", true);
  });
});

function cell() {
  this
      .style("left", function(d) { return d.x + "px"; })
      .style("top", function(d) { return d.y + "px"; })
      .style("width", function(d) { return Math.max(0, d.dx - 1) + "px"; })
      .style("height", function(d) { return Math.max(0, d.dy - 1) + "px"; })
      .style("text-align", "center")
      .style("cursor", "pointer")
      
	  
	  
	  
}
