import {ChatElement} from "./ChatElement.js";

export class Chat {
    constructor(csrf) {
        this.maxDrawnId = 0;
        this.elementsArray = [];
        this.parentElement = $("#chat");
        this.sendButton = $("#send-btn");
        this.input = $("#chat-input");
        this.toClear = true;

        this.csrf = csrf;

        this.getUrl = "api/messages";
        this.postUrl = "api/messages/create";

        this.addListeners();
    }

    async refreshTime() {
        this.elementsArray.forEach(element => {
            element.refreshTime();
        })
    }

    sendMessage() {
        let messageText = this.input.val();
        let data = {
            body: messageText
        }
        let that = this;

        $.ajax({
            url: that.postUrl,
            type: 'POST',
            data: data,
            beforeSend: function (xhr) {
                xhr.setRequestHeader("X-CSRFToken", that.csrf);
            },
            success: function () {
                that.draw();
                that.input.val("");
            }
        })
    }

    addListeners() {
        let that = this;
        this.sendButton.click(function () {
            that.sendMessage()
        });
        this.input.keypress("keypress", function (e) {
            if (e.key === "Enter") {
                that.sendMessage();
            }
        });
    }


    draw() {
        let that = this;
        $.ajax({
            url: that.getUrl,
            success: function (data) {
                if (that.toClear) {
                    that.parentElement.empty();
                    that.toClear = false;
                }
                let results = data.results.reverse();
                let element;

                results.forEach(elementData => {
                    if (elementData.id > that.maxDrawnId) {
                        element = new ChatElement(elementData);
                        let pl = that.parentElement;
                        let atBottom = Math.abs(pl.offset().top) + pl.height() + pl.offset().top >= pl.outerHeight();
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


