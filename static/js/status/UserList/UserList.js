import {UserListElement} from "./UserListElement.js";

export class UserList {
    constructor() {
        this.drawnIdArray = [];
        this.drawnElementArray = [];
        this.parentElement = $("#present-lab-users");
        this.spinnerElement = $("#present-lab-users-spinner");
        this.tableElement = $("#show-table");
        this.emptyElement = $("#show-table-empty");
        this.toClear = true;

        this.url = "api/lab-users-present";
    }

    async refreshTime() {
        this.drawnIdArray.forEach(element => {
            element.refreshTime();
        })
    }

    draw() {
        let that = this;
        $.ajax({
            url: that.url,
            success: function (data) {
                if (that.toClear) {
                    that.spinnerElement.remove();
                    that.toClear = false;
                }
                let element;
                let presentUsersIdArray = [];
                data.forEach(elementData => {
                    if (!that.drawnIdArray.includes(elementData.id)) {
                        element = new UserListElement(elementData);
                        that.parentElement.append(element.drawElement());
                        that.drawnIdArray.push(elementData.id);
                        that.drawnElementArray.push(element);
                    }
                    presentUsersIdArray.push(elementData.id);
                })

                that.drawnElementArray.forEach(element => {
                    if (!presentUsersIdArray.includes(element.data.id)) {
                        let indexEA = that.drawnElementArray.indexOf(element);
                        let indexIA = that.drawnIdArray.indexOf(element.data.id);
                        element.removeElement();
                        if (indexEA > -1) {
                            that.drawnElementArray.splice(indexEA, 1);
                            that.drawnIdArray.splice(indexIA, 1);
                        }
                    }
                })
                if (that.drawnIdArray.length) {
                    that.tableElement.removeClass("d-none");
                    that.emptyElement.addClass("d-none");
                } else {
                    that.tableElement.addClass("d-none");
                    that.emptyElement.removeClass("d-none");

                }
            }
        })
    }
}