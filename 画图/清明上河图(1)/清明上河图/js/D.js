var tool=function(){
	var D=document, ua = navigator.userAgent.toLowerCase(), isOpera = (ua.indexOf('opera') > -1), isIE = (!isOpera && ua.indexOf('msie') > -1);
		return {
		Linear: function(t,b,c,d){ return t*c/d + b; },
		$:function(ele,b){
			var a,f='';
			if(ele.indexOf(".")!=-1){
				a=ele.substr(1);
				var c = [],d = new RegExp("\\b" + a + "\\b"),e = D.getElementsByTagName(b || "*"),len=e.length;
				for (var h = 0; h < len; h++) {
					f=e[h].className;
					if (d.test(f)) {c.push(e[h])}
				};
				return c;
			};
			if(ele.indexOf("#")!=-1){  
				a=ele.substr(1);
				var c = (a && typeof a != "string") ? a: D.getElementById(a);
				return (!b ? c: c.getElementsByTagName(b));
			}
		},// $("#id","ele") $(".class","ele")
		cancelClick: function(e) {
			if (window.event) {
				window.event.cancelBubble = true;
				window.event.returnValue = false;
			}
			if (e && e.stopPropagation && e.preventDefault) {
				e.stopPropagation();
				e.preventDefault();
			}
		},
		scrollXY:function(e){
			if(e=="scrollLeft"||e=="scrollTop"){
				return self.pageXOffset || D.documentElement[e] || D.body[e];
			}else{alert("wrong")}
		},//scrollW
		broswerXY:function(e){
			if(e=="clientWidth"||e=="clientHeight"){
				var j = self.innerWidth,k = D.compatMode;
				if ((k || isIE) && !isOpera) {
					j = (k == "CSS1Compat") ? D.documentElement[e] : D.body[e];
				}
				return j;
			}else{alert("wrong")}
		},//broswerXY
		rect:function(node){
			var left = 0, top = 0, right = 0, bottom = 0;
			if ( !node.getBoundingClientRect ) {
				var n = node;
				while (n) { left += n.offsetLeft, top += n.offsetTop; n = n.offsetParent; };
				right = left + node.offsetWidth; bottom = top + node.offsetHeight;
			} else {
				var rect = node.getBoundingClientRect();
				left = right = this.scrollXY("scrollLeft"); top = bottom = this.scrollXY("scrollTop");////this
				left += rect.left; right += rect.right;
				top += rect.top; bottom += rect.bottom;
			};
		return { "left": left, "top": top, "right": right, "bottom": bottom };
		},//rect
		mouse:function(){
			return{
				x:function(e){
					return isIE?window.event.clientX+D.body.scrollLeft+D.documentElement.scrollLeft:e.pageX;
				},
				y:function(e){
					return isIE?window.event.clientY+D.body.scrollTop+D.documentElement.scrollTop:e.pageY;
				}
			}
		}()//mouse
	}//return
}();