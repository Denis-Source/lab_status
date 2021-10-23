import {PartElement} from "./PartElement.js";


export class PartLightElement extends PartElement {
    constructor(partName, csrf) {
        super(partName);

        this.csrf = csrf;
        this.urlAuto = "api/parts/light/auto";
        this.urlStatus = "api/parts/light/status";

        this.spinnerAutoElement = $("#light-spinner-auto");

        this.parentElement = $("#light-card");

        this.autoElementButton = $("#light-card-top-button");
        this.statusElementButton = $("#light-card-bottom-button");

        this.autoText = $("#light-card-auto");
        this.addListeners();
    }

    addListeners() {
        let that = this;

        this.statusElementButton.click(function () {
            that.loadingOn();
            that.loadingAutoOn();
            $.ajax({
                url: that.urlAuto,
                method: "PUT",
                data: {auto: false},
                headers: {"X-CSRFToken": that.csrf},
                success: function (data) {
                    that.updateElementAuto(data.auto);
                    $.ajax({
                        url: that.urlStatus,
                        method: "PUT",
                        data: {status: !that.data.status},
                        headers: {"X-CSRFToken": that.csrf},
                        success: function (data) {
                            that.updateElementStatus(data.status);
                        }
                    })

                }
            })
        });

        this.autoElementButton.click(function () {
            that.loadingAutoOn();
            $.ajax({
                url: that.urlAuto,
                method: "PUT",
                data: {auto: !that.data.auto},
                headers: {"X-CSRFToken": that.csrf},
                success: function (data) {
                    that.updateElementAuto(data.auto);
                }
            })
        });
    }

    loadingAutoOff() {
        this.spinnerAutoElement.addClass("d-none");
        this.autoText.removeClass("d-none");
    }

    loadingAutoOn() {
        this.spinnerAutoElement.removeClass("d-none");
        this.autoText.addClass("d-none");
    }

    drawElement(data) {
        super.drawElement(data);
        if (data.auto) {
            this.autoText.text("auto");
        } else {
            this.autoText.text("manual");
        }
        this.loadingAutoOff();
    }

    updateElementAuto(newAuto) {
        this.data.auto = newAuto;
        if (newAuto) {
            this.autoText.text("auto");

        } else {
            this.autoText.text("manual");
        }
        this.loadingAutoOff();
    }
}