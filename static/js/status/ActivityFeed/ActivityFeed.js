import {ActivityFeedElement} from "./ActivityFeedElement.js";

export class ActivityFeed {
    constructor() {
        this.maxDrawnId = 0;
        this.elementsArray = [];
        this.parentElement = $("#activity-feed");
        this.toClear = true;

        this.url = "api/events";
    }

    async refreshTime() {
        this.elementsArray.forEach(element => {
            element.refreshTime();
        })
    }


    draw() {
        let that = this;
        $.ajax({
            url: that.url,
            success: function (data) {
                let results = data.results.reverse();
                if (that.toClear) {
                    that.parentElement.empty();
                    that.toClear = false;
                }
                results.forEach(elementData => {
                    if (elementData.id > that.maxDrawnId) {
                        let element = new ActivityFeedElement(elementData);
                        let pl = that.parentElement;
                        let atBottom = pl[0].scrollHeight - pl.scrollTop() === pl.outerHeight()
                        that.parentElement.append(element.drawElement());
                        that.elementsArray.push(element);
                        that.maxDrawnId = elementData.id;
                        if (atBottom) {
                            pl.scrollTop(pl[0].scrollHeight);
                        }
                    }
                })
            }
        })
    }
}