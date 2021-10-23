import {PartElement} from "./PartElement.js";
import {PartVentElement} from "./PartVentElement.js";
import {PartLightElement} from "./PartLightElement.js";

export class PartsStatus {
    constructor(csrf) {
        this.url = "api/parts";

        this.csrf = csrf;
        this.lightElement = new PartLightElement("light", this.csrf);
        this.ventElement = new PartVentElement("vent", this.csrf);
        this.movementElement = new PartElement("movement");
        this.doorElement = new PartElement("door");
    }

    draw() {
        let that = this;
        $.ajax({
            url: that.url,
            success: function (data) {
                data.forEach(elementData => {
                    switch (elementData.name) {
                        case "light": that.lightElement.drawElement(elementData);
                        break;
                        case "vent": that.ventElement.drawElement(elementData);
                        break;
                        case "movement": that.movementElement.drawElement(elementData);
                        break;
                        case "door": that.doorElement.drawElement(elementData);
                        break;
                    }
                })
            }
        })
    }
}