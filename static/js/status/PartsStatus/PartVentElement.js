import {PartElement} from "./PartElement.js";

export class PartVentElement extends PartElement {
    constructor(partName, csrf) {
        super(partName);
        this.csrf = csrf;

        this.url = "api/parts/vent/status"
        this.selector = $("#vent-card");
        this.addListener();
    }

    addListener() {
        let that = this;
        this.selector.click(function () {
            that.loadingOn();
            $.ajax({
                url: that.url,
                method: "PUT",
                data: {status: !that.data.status},
                headers: {"X-CSRFToken": that.csrf},
                success: function (data) {
                    that.updateElementStatus(data.status);
                }
            })
        });
    }
}