# SAPUI5

## 1 Header Must-Have
`<!DOCTYPE html>`
to tell the document is written in html5.<br/>
`<meta http-equiv="X-UA-Compatible" content="IE=edge">` to tell Microsoft Internet Explorer (whoever is still using it) to use the latest rendering engine (Edge).<br />
`<meta charset="utf-8">` tells the browser that your files are encoded in
UTF-8. <br />
Obviously you can also include a `<title>` (you don't have to but it is very
useful).

### 1.1 SAP initialization
#### 1.1.1 Include SAP
```html
<script src="http://<<server>>:<<port>>/resources/sap-ui-core.js"
  id="sap-ui-bootstrap">
</script>
```
includes and initializes sap. If you're  working directly on the server you can also simply use `/resources/sap-ui-core.js` as source. You still need to include the id and the data. There are also several options that you can provide, such as:
* `data-sap-ui-theme="sap_belize"` which sets the default theme to sap_belize
* `data-sap-ui-libs="sap.m"` sets the default UI-Library. sap.m includes
UI-elements like Texts, Buttons, a.s.o. (Click [here](#sap_controls) for a
list + description).
* `data-sap-ui-compatVersion="edge"` sets the compatibility version of sap to
the one of Microsoft Edge (analog to the `<meta>`-tag in the header). This binding is needed when you for example want to combine static text with a variable. The standard syntax only allows static text OR variables.
* `data-sap-ui-preload="async"` makes sure that the SAP resources can be
loaded simultaneously in the background. This has performance reasons.

#### 1.1.2 Add apps and pages
##### Apps
Next thing you need to do is calling sap's `sap.ui.getCore().attachInit()` to create a new app. The code for it looks like the following:
```javascript
//Calls sap's attachInit with a function as parameter
sap.ui.getCore().attachInit(function () {
	// create a mobile app and display page1 initially
	var app = new sap.m.App("myApp", {
		initialPage: "page1"
	});
});
```
Notice that we're setting the initialPage even though there is no "page1" yet. It get's created in the next step:

##### Pages
A page uses SAP's sap.m.Page-class. An example code would look like the following:
```javascript
var page1 = new sap.m.Page("page1", {
	title : "Hello World",
	showNavButton : false,
	content : new sap.m.Button({
		text : "Go to Page 2",
		press : function () {
			// navigate to page2
			app.to("page2");
		}
	})
});
```
Notice that you have two attributes - a page name and an object that contains information like the title, content and a mysterious `showNavButton`. This is nothing more than just a back button which calls `app.back()` which brings the user back to the main page. `false` obviously disables the button (meaning it is not visible) - `true` enables it.

Pages get added to the website via the `app.addPage(sap.m.Page page)` method \- in this case `app.addPage(page1)`. More pages can be added by calling the `addPage` multiply times (e.g. `app.addPage(page1).addPage(page2)` a.s.o.).

#### Include the app in HTML
At the end you need to add the app to the website. Therefore you simply call the `app.placeAt(String html_id)`-method that places the html code to the html-element with the given id. In this case this is the `body` with the id "content" - `app.placeAt("content")`.

<style>
  ul a, ul a:active, ul a:visited, ul a:hover, ul a:link {
  font-weight: bold;
  text-decoration: none;
  }
</style>

## 2 SAP Controls
* <a name="text" href="https://openui5.hana.ondemand.com/#/api/sap.m.Text/controlProperties">sap.m.Text</a><br />
  * <i>functionality</i>: View some text
  * <i>comparable HTML-element</i>: `<p>`
  * <i>important attributes</i>:
    * <u>text</u>: the content of the text
* <a name="button" href="https://openui5.hana.ondemand.com/#/api/sap.m.Button/controlProperties">sap.m.Button</a><br />
  * <i>functionality</i>: A button that is clickable
  * <i>comparable HTML-element</i>: `<button>` or `<input type="button">`
  * <i>important attributes</i>:
    * <u>text</u>: the value of the button
    * <u>press</u>: the button-event; similar to `onclick`; inclusion comes
    with the controller.
* <a name="input" href="https://openui5.hana.ondemand.com/#/api/sap.m.Input/controlProperties">sap.m.Input</a><br />
  * <i>functionality</i>: An input field for user interaction
  * <i>comparable HTML-element</i>: `<input [type="text"]>`
  * <i>important attributes</i>:
    * <u>value</u>: the default value of the input text; if connected to a [Model](#json_model) it updates the value of the model if valueLiveUpdate is true
    * <u>description</u>: a description for the input field; It is placed on the right side of the field
    * <u>valueLiveUpdate</u>: either true or false; says whether the value in the model is updated live or not (otherwise it is probably after an event occuring)
* <a name="page" href="https://sapui5.hana.ondemand.com/#/api/sap.m.Page/controlProperties">sap.m.Page</a><br />
  * <i>functionality</i>: Displays a page that has 0 to N other controls (which are included as `<content>`-tags)
  * <i>comparable HTML-element</i>: `<body>`
  * <i>important attributes</i>:
    * <u>title</u>: the page title
* <a name="panel" href="https://sapui5.hana.ondemand.com/#/api/sap.m.Panel/controlProperties">sap.m.Panel</a><br />
  * <i>functionality</i>: Groups related content
  * <i>comparable HTML-element</i>: `<div>`
  * <i>important attributes</i>:
    * <u>headerText</u>: a text placed on top of the panel that works as a headline and short descriptor
    * <u>height</u>: the height of the panel
    * <u>width</u>: the width of the panel
* <a name="app href="https://sapui5.hana.ondemand.com/#/api/sap.m.App/controlProperties">sap.m.App</a><br />
  * <i>functionality</i>: Writes several properties into the header (which are necessary for proper display on mobile devices) and adds functionality to navigate between pages; The pages of the app are added in a `<pages>`-tag. E.g.:
  ```html
    <App>
      <pages>
        <Page title="page1" />
        <Page title="page2" />
        <Page title="page3" />
      </pages>
    </App>
  ```
  * <i>comparable HTML-element</i>: `<html>`
* <a name="dialog" href="https://sapui5.hana.ondemand.com/#/api/sap.m.Dialog/controlProperties">sap.m.Dialog</a><br />
* <i>functionality</i>: a dialog to prompt the user for an action or confirmation; it interrupts the current app as it is the only focused UI element and background is dimmed and blocked;
* <i>comparable JavaScript-element</i>: `alert`
* <i>important attributes</i>:
  * <u>title</u>: the title of the dialog
* <a name="ObjectListItem" href="https://sapui5.hana.ondemand.com/#/api/sap.m.ObjectListItem/controlProperties">sap.m.ObjectListItem</a><br />
  * <i>functionality</i>: ObjectListItem is a control item that is good for displaying objects since it has a nice formatting for several nice attributes that sum up to a good description;
  * <i>comparable HTML-element</i>: `<ul>` with `<li>` and `bootstrap`-formatting
  * <i>important attributes</i>:
    * <u>intro</u>: short introduction text to the item
    * <u>title</u>: title of the item
    * <u>icon</u>: icon displayed left of the title
    * <u>number</u>: a number like e.g. a price or something like this
    * <u>numberUnit</u>: the unit of the number
    * <u>numberState</u>: defines the value of the number
* <a name="title" href="https://sapui5.hana.ondemand.com/#/api/sap.m.Title/controlProperties">sap.m.Title</a><br />
  * <i>functionality</i>:
  * <i>comparable HTML-element</i>:
  * <i>important attributes</i>:
    * <u>text</u>:
* <a name="" href="https://sapui5.hana.ondemand.com/#/api/sap.m./controlProperties">sap.m.</a><br />
  * <i>functionality</i>:
  * <i>comparable HTML-element</i>:
  * <i>important attributes</i>:
    * <u>text</u>:


## 3 XML
Since we don't want the header to be way too long and there is an option for preventing this why wouldn't we use it? The tool we are using for this is XML.
### 3.1 XML View
#### 3.1.1 Main App
First we need to create the main app (similar to the `sap.m.App`-object in the header) file. This can basically be called `App.view.xml` as a standard although you could give it any name you want.<br />
The base syntax for the app is
```xml
<mvc:View
   xmlns="sap.m"
   xmlns:mvc="sap.ui.core.mvc">
</mvc:View>
```
Note that the first `xmlns="sap.m"` just makes the XML-File use the sap.m namespace as the standard namespace. `xmlns:mvc` creates a namespace "mvc" for "sap.ui.core.mvc" (so you don't have to write the whole thing over and over).

### 3.2 Tagging the XML in the HTML-file
Include
```html
<script
[...]
data-sap-ui-resourceroots='{
  "sap.ui.demo.walkthrough": "./"
}'>
```
in the SAP initialization. This will tell the SAPUI5 core that the resources in the given namespace (in this case "sap.ui.demo.walkthrough") are located in the same folder as the html-file.

Next you need to add the XML-File to the `attachInit()`-method. At the end it should like this:
```javascript
sap.ui.getCore().attachInit(function () {
   sap.ui.xmlview({
      viewName : "sap.ui.demo.walkthrough.view.App"
   }).placeAt("content");
});
```
Notice that you can leave out the ".view.xml" at the end of the file name.

### 3.3 XML Controller
To add user interaction (like pressing a [button](#button)) you need to add a controller. This controller gets tagged via
```javascript
controllerName="sap.ui.demo.walkthrough.controller.App"
```
where the name of the controller is `App.controller.js`. The controller has to be located in the "controller"-folder and it's inclusion must not include the ".controller.js"-part. The base of the controller looks like the this:
```javascript
sap.ui.define([
   "sap/ui/core/mvc/Controller"
], function (Controller) {
   "use strict";
   return Controller.extend("", {
   });
});
```
> The "use strict" [...] tells the browser to execute the code in a so called “strict mode”. The strict mode [...], for example, makes sure that variables are declared before they are used. [...] This helps to prevent common JavaScript pitfalls.<br />
 \- [SAP Hana Tutorial Note](https://sapui5.hana.ondemand.com/#/topic/50579ddf2c934ce789e056cfffe9efa9)

The next thing to focus on is the `extend`-method from the controller. It provides the functionality for the user interaction by handling the different events.

If we now, for example, had a button that was defined in the XML like that:
```XML
<Button
      text="Say Hello"
      press="onShowHello"/>
```
then we can handle this event with something like this:
```JavaScript
[...]
return Controller.extend("sap.ui.demo.walkthrough.controller.App", {
  onShowHello : function () {
     // show a native JavaScript alert
     alert("Hello World");
  }
});
[...]
```
Notice that the first parameter of the `extend`-method has the same name as the one given in the view. In this case when the user clicks the button "Say Hello" there will be an alert saying "Hello World". Whoa, pretty sick.

But, as you might know, the standard Browser alerts are pretty boring right?
<br />Well, SAP knows this and they included a Message Toast in their sap.m-library. And this looks ways better than the default alert.<br />
The inclusion is pretty basic, you add `"sap/m/MessageToast"` to the array, add `MessageToast` as a parameter for the function afterwards and now you can use it in the `extend`-method. For example via `MessageToast.show("Hello World")`.

### 3.4 Component
The component is a SAP-provided object that takes care of initialization and is kind of an extension to the static `index.html`-file. The component also works as an extension for the controller especially in terms of initialization, he makes it a lot easier for the developer, since he gets to know the view and the model.

The component extends from the `UIComponent`, since he has the same form as the controller, he needs to add it to the array and as a parameter to its function. In the function, the `extend`-method gets called. There we have an init-function, where the component gets initialized. This looks something like this:
```javascript
sap.ui.define([
   "sap/ui/core/UIComponent"
], function (UIComponent) {
   "use strict";
   return UIComponent.extend("", {
      init : function () {
         // call the init function of the parent
         UIComponent.prototype.init.apply(this, arguments);
	      }
   });
});
```
I told you that the component knows about the view and the model - well therefore we need to modify the `extend`-method a little bit:
```javascript
[...]
metadata : {
  rootView: {
    "viewName": "sap.ui.demo.walkthrough.view.App",
    "type": "XML",
    "async": true,
    "id": "app"
  }
},
[...]
```
And because of that beautiful component we have there, we don't even need anything than that in the `atachInit`-function. It now looks like this:
```javascript
sap.ui.getCore().attachInit(function () {
   new sap.ui.core.ComponentContainer({
      name : "sap.ui.demo.walkthrough"
   }).placeAt("content");
```

### 3.5 Shell Control
Next thing to do is adding a shell control for better device support - the shell takes care of the visual adaption of the app via a so-called "letterbox". The shell gets included in the `attachInit`-function, which after adaption looks like this:
```JavaScript
sap.ui.getCore().attachInit(function () {
   new sap.m.Shell({
     // note that there's still the ComponentContainer for the component
      app : new sap.ui.core.ComponentContainer({
         name : "sap.ui.demo.walkthrough",
         settings : {
             id : "walkthrough"
         }
      })
   }).placeAt("content");
});
```

### 3.6 JSON Model
Sometimes you need to store some data, this won't happen to often though, so we can theoretically skip this topic right away, right? Well, just kidding, data is one of the most important parts of SAP and having a Model means storing this data. SAP's Model uses JSON for it and therefore needs a `JSONModel`, which you need to add to the array right away (it's path is "sap/ui/model/json/JSONModel"). Afterwards - like with the `MessageToast` for the controller you need to add this object to the Component-function: Just add `JSONModel` as a parameter.<br />
Now with the initialization of the component you can add some data as a JSON object. This could look something like this:
```JavaScript
[...]
init : function () {
  [...]
   // set data model on view
   var oData = {
      recipient : {
         name : "World"
      }
   };
   var oModel = new JSONModel(oData);
   this.setModel(oModel);
},
[...]
```
In the view you can now easily use this data via curly brackets ("{}") - so called "data binding" - and the reference for the object. This could look like that
```xml
<Input
   value="{/recipient/name}"
   description="Hello {/recipient/name}"
   valueLiveUpdate="true"
   width="60%"/>
```
Here we have an [Input](#input)-field that has the value "World" (because we set it in the controller) and a description (which is located on the right side of the input) that changes with the value (via `valueLiveUpdate`).

### 3.7 Properties
To make texts easily translate- and changable, you can move them to a specific file. This process is called internationalization - short i18n - and this is the place where the static data gets stored: In the `/i18n/i18n_countryCode.properties`-file. Here you can create variables and stuff by simple key=value stores - and you don't need any quotes or something.

Adding these variables to the component requires a `ResourceModel`-object ("/sap/ui/model/resource/ResourceModel") which you - again - need to add to the parameter-list. Then you need to initialize the properties to the model and set it to the view (do it in the `onInit`):
```JavaScript
// set i18n model on view
var i18nModel = new ResourceModel({
   bundleName: "sap.ui.demo.walkthrough.i18n.i18n"
});
this.setModel(i18nModel, "i18n");
```
Since we are also showing the message in a `MessageToast` in the controller, we need to load the message from the i18n model:
```JavaScript
// read msg from i18n model
var oBundle = this.getView().getModel("i18n").getResourceBundle();
var sRecipient = this.getView().getModel().getProperty("/recipient/name");
// set the variable of helloMsg
var sMsg = oBundle.getText("helloMsg", [sRecipient]);
// show message
MessageToast.show(sMsg);
```
Notice that the controller has no clue, what exactly the view or the model is - and that's why he uses the `getView()` and `getModel()` functions.<br />
With the `i18n.properties`-file including `helloMsg=Some Message {0}`, where `{0}` is the variable part of the text (e.g. an input of the user).

#### 3.7.1 i18n in View
Using internationalization in the View again uses data binding ("{}") - but now not with slashes but with angle brackets - `{i18n>variable}`. The part before the angle bracket is the model name that got set in the component.


## 4 SAP configuration
The SAP configuration is usually put in a descriptor file called `manifest.json`. This helps separating the settings from the components allowing multiple apps to be displayed in the same context., whilst still having local settings like language properties and more. There is also the possibility of loading and instantiating models like the i18n resource bundle. An example `manifest.json` could look like this:
```json
{
  "_version": "1.8.0",
  "sap.app": {
	"id": "sap.ui.demo.walkthrough",
	"type": "application",
	"i18n": "i18n/i18n.properties",
	"title": "{{appTitle}}",
	"description": "{{appDescription}}",
	"applicationVersion": {
	  "version": "1.0.0"
	}
  },
  "sap.ui": {
	"technology": "UI5",
	"deviceTypes": {
		"desktop": true,
		"tablet": true,
		"phone": true
	}
  },
  "sap.ui5": {
	"rootView": {
		"viewName": "sap.ui.demo.walkthrough.view.App",
		"type": "XML",
		"async": true,
		"id": "app"
	},
	"dependencies": {
	  "minUI5Version": "1.30",
	  "libs": {
		"sap.m": {}
	  }
	},
	"models": {
	  "i18n": {
		"type": "sap.ui.model.resource.ResourceModel",
		"settings": {
		  "bundleName": "sap.ui.demo.walkthrough.i18n.i18n"
		}
	  }
	}
  }
}
```
Since we are also using variables from the `i18n.properties`-file here, we need to add them to the file. In this case, this are the "appTitle" and an "appDescription":
```
appTitle=Some app title
appDescription=What a beautiful app right?
```

In the component (`Component.js`), we can redefine the metadata to use the a JSON-file as manifest:
```JavaScript
[...]
metadata : {
      manifest: "json"
},
[...]
```
An explanation for the different variables of the `manifest.json`-file can be found [here](https://sapui5.hana.ondemand.com/#/topic/8f93bf2b2b13402e9f035128ce8b495f).

## 5 Making the app beautiful
### 5.1 Margins and Paddings
Adding some margins and paddings always helps with responsive websites. SAPUI5 is no exception. In this case there are some default classes that will be used for providing this responsiveness.
#### 5.1.1 Panel
The margin in the panel will be added via the `sapUiResponsiveMargin`-class. Next to this class we need to set the width to "auto" since otherwise the margin would be added to the default width of 100% and exceed the page.
#### 5.1.2 Components
The classes used for components can be something like `sapUiSmallMarginEnd` or `sapUiSmallMargin` - classes that add some margin that the elements don't stick together to hard but also don't have light years of distance between each other. Since SAP already provides these default margin classes, use them, it would be unnecessary to write your own classes for this.<br />
<i>Note</i>: the default classes are `sapUi<Tiny|Small|Medium|Large>Margin[Top|Bottom| Begin|End]` where in the first case is a value needed whilst the second one can be left out. Another look at predefined css classes can be seen [here](https://sapui5.hana.ondemand.com/#/topic/777168ffe8324873973151dae2356d1c.html).

### 5.2 Custom CSS
Of course there are no default classes for every case and so sometimes the developer needs to write his own css files. Therefore you can easily create a file and save it unser "/css". Then, in the `manifest.json`-file under `sap.ui5` and `models`, if not already existing, add this:
```json
[...]
"resources": {
  "css": [
  {
    "uri": "css/style.css"
  }
  ]
}
[...]
```
If there is already an array with the key "css", simply add more items to the list. So, multiple css-sources would look like this:
```json
[...]
"css": [
  {
    "uri": "css/style.css"
  },
  {
    "uri": "css/style2.css"
  },
  [...]
]
[...]
```
The classes can be added in the `class`-attribute.

### 5.3 Dialogs and Fragments
I've already told you that there was a much more beautiful solution to the browsers alerts (`MessageToast`s) but to be honest - they are more of a notification box, no alert. But SAP provides another pretty beautiful alternative to alerts: fragments. A fragment consists of multiple controls (at least 1 though). What now makes a dialog so special: It isn't part of the currently viewed app meaning it stands out of it. It kind of emits from the website and therefore really emphasizes a message - like an alert just more beautiful.
#### 5.3.1 The fragment view
The view for the fragment is again its own file. Since it is not a view or a panel it has to have its own kind of file name: `dialogName.fragment.xml` (or JavaScript-representation if you chose this option). This file now doesn't extend from SAPs UI but more from SAPs `sap.ui.core`. It also includes the `sap.m` as the standard namespace like the default view.<br/>
Since this fragment is going to have a dialog in it (like I said we want to have a more beautiful alert), it consists of a [`sap.m.Dialog`](#dialog)-object. In the an xml-file would look something like this:
```xml
<core:FragmentDefinition
   xmlns="sap.m"
   xmlns:core="sap.ui.core" >
   <Dialog
      id="helloDialog"
      title ="Hello {/recipient/name}">
      <beginButton>
         <Button
            text="{i18n>dialogCloseButtonText}"
            press="onCloseDialog"/>
      </beginButton>
   </Dialog>
</core:FragmentDefinition>
```
Note that here is already a callback button included that fires the onCloseDialog-event.
#### 5.3.2 The dialog in the component
To make the dialog reusable and to not have to create it once again everytime we are going to create a new JavaScript-file called `DialogName.js`. This file creates an `DialogName`-object via which we can eventually manage the object in the componenet. The `DialogName.js`-file (let's call it "HelloDialog" for once) looks something like this:
```JavaScript
sap.ui.define([
	"sap/ui/base/ManagedObject"
], function (ManagedObject) {
	"use strict";
	return ManagedObject.extend("sap.ui.demo.walkthrough.controller.HelloDialog", {
		constructor : function (oView) {
			this._oView = oView;
		},

    // if the user closes the dialog:
    //    kill the connection to the view
    //    -> free up space the dialog would use
    //    -> the view of the dialog will kill itself automatically
		exit : function () {
			delete this._oView;
		},

		open : function () {
			var oView = this._oView;
			var oDialog = oView.byId("helloDialog");

			// create dialog lazily
      // -> check if the dialog was already created once
			if (!oDialog) {
				var oFragmentController = {
					onCloseDialog : function () {
						oDialog.close();
					}
				};
				// create dialog via fragment factory
				oDialog = sap.ui.xmlfragment(oView.getId(), "sap.ui.demo.walkthrough.view.HelloDialog", oFragmentController);
				// connect dialog to the root view of this component (models, lifecycle)
				oView.addDependent(oDialog);
			}
			oDialog.open();
		}
	});
});
```
Note that the constructor requires a view (which is the current page).
What you can do now is adding the dialog to the component:
```JavaScript
sap.ui.define([
  [...]
	"sap/ui/demo/walkthrough/controller/HelloDialog"
], function (UIComponent, JSONModel, HelloDialog) {
  [...]
	return UIComponent.extend("sap.ui.demo.walkthrough.Component", {
    [...]
			// set dialog
			this._helloDialog = new HelloDialog(this.getRootControl());
		},

    // if this app exits, kill the dialog!
		exit : function() {
			this._helloDialog.destroy();
			delete this._helloDialog;
		},

		openHelloDialog : function () {
			this._helloDialog.open();
		}
    [...]
```
Since we still need to open the dialog we need to modify both the main app (Spoiler: which will later become the `HelloPanel.view.xml`) and the main controller (Spoiler: this is gonna turn into the `HelloPanel.controller.js`):
The main view gets a new button that opens the dialog - just add this element:
```xml
<button
  text="{i18n>openDialogButtonText}"
  press="onOpenDialog"
  class="sapUiSmallMarginEnd"/>
```
The controller on the other hand obviously needs to control the dialog - it at least needs to open it. Therefore add the `onOpenDialog`-event to it:
```javascript
onOpenDialog : function () {
  this.getOwnerComponent().openHelloDialog();
}
```
<strong>Attention!</strong> Later, you'll move the controller to a new file - keep the `onOpenDialog` in both files. It is easier for you to instanciate from it when creating a new app.


## 6 Making the code more beautiful
### 6.1 Nested Views
Embedding views in other views is a very nice function if you want to keep your project organized and, especially for larger projects, that helps you with focusing on one specific task at a time. So, what you need to do is creating a new view that follows the same rules as the main xml file:
```xml
<mvc:View
   controllerName="sap.ui.demo.walkthrough.controller.HelloPanel"
   xmlns="sap.m"
   xmlns:mvc="sap.ui.core.mvc">
   <Panel
      headerText="{i18n>helloPanelTitle}"
      class="sapUiResponsiveMargin"
      width="auto" >
      <content>
         <Button
            text="{i18n>showHelloButtonText}"
            press="onShowHello"
            class="myAppDemoWT myCustomButton"/>
         <Input
            value="{/recipient/name}"
            valueLiveUpdate="true"
            width="60%"/>
         <FormattedText
            htmlText="Hello {/recipient/name}"
            class="sapUiSmallMargin sapThemeHighlight-asColor myCustomText"/>
      </content>
   </Panel>
</mvc:View>
```
As you can see here, we have the namespacing, the controllerName and the components of the page.<br />
Now this page can be included via the `XMLView` in the `sap.ui.core.mvc`- or simply the namespace `mvc` - library. The specific file can be embedded with the parameter `viewName` which will obviously be set to the name of the view - if the view is called `HelloPanel.view.xml` then this name is "sap.ui.your.project.view.HelloPanel" (you can compare it to the controller name).

### 6.2 New view - new controller
A new view (obviously) requires a new controller. This can be achieved relatively easy: Just create a new one. The structure is always the same: Create a array for all the requirements, add them to the function as a parameter and then extend the controller for the events. A `HelloController` in this case would look like this:
```JavaScript
sap.ui.define([
   "sap/ui/core/mvc/Controller",
   "sap/m/MessageToast"
], function (Controller, MessageToast) {
   "use strict";
   return Controller.extend("sap.ui.demo.walkthrough.controller.HelloPanel", {
      onShowHello : function () {
         // read msg from i18n model
         var oBundle = this.getView().getModel("i18n").getResourceBundle();
         var sRecipient = this.getView().getModel().getProperty("/recipient/name");
         var sMsg = oBundle.getText("helloMsg", [sRecipient]);
         // show message
         MessageToast.show(sMsg);
      }
   });
});
```
Since this is the same as in the main controller, we can simply delete this one. This leads to the main app and main controller being nearly completely empty - and the main functionalities are separated from each other.

## 7 Data handling
### 7.1 Displaying data
Let's create some dummy data and save it as JSON-formatted file (e.g. `Invoices.json` [yeah, I'm copying this, but I'm just gonna give you two dummy datasets...]):
```json
{
  "Invoices": [
	{
	  "ProductName": "Pineapple",
	  "Quantity": 21,
	  "ExtendedPrice": 87.2000,
	  "ShipperName": "Fun Inc.",
	  "ShippedDate": "2015-04-01T00:00:00",
	  "Status": "A"
	},
  [...]
	{
	  "ProductName": "Bread",
	  "Quantity": 1,
	  "ExtendedPrice": 2.71212,
	  "ShipperName": "Fun Inc.",
	  "ShippedDate": "2015-01-27T00:00:00",
	  "Status": "C"
	}
]
}
```
What you can do now is going into that `manifest.json` file. Under `sap.ui5`, you'll find a `models`-JSON-object. Get in there and create a new key called "invoice" and add your just created beautiful file as a dataset:
```json
"invoice": {
  "type": "sap.ui.model.json.JSONModel",
  "uri": "Invoices.json"
}
```
Now in our main view (`App.view.xml`), we'll add another view because structure and organization. Let's call the new view `InvoiceList` since we are creating a list of invoices. Sounds legit right? So the new view file is going to be called `InvoiceList.view.xml` and it looks like this:
```xml
<mvc:View
   xmlns="sap.m"
   xmlns:mvc="sap.ui.core.mvc">
   <List
      headerText="{i18n>invoiceListTitle}"
      class="sapUiResponsiveMargin"
      width="auto"
      items="{invoice>/Invoices}" >
      <items>
         <ObjectListItem
            title="{invoice>Quantity} x {invoice>ProductName}"/>
      </items>
   </List>
</mvc:View>
```
As you can see it uses the `invoice`-dataset we created in the manifest to create a [list](#list) of invoices. The display is pretty standard right now but SAP still formats it pretty nicely for us so we don't need to take for that. What's interesting to see is that you can easily use the keys of the JSON-file. Fantastic!<br />
Note that the used item type here is [`ObjectListItem`](#objectlistitem) which is pretty helpfulm in terms of displaying an object nicely formatted.
The next thing we're gonna do is include this file into the main app:
```xml
<mvc:XMLView viewName="sap.ui.demo.walkthrough.view.InvoiceList"/>
```
Save it all, reload the page and boom, you should see all of those entries you created (hopefully more than 2...).

### 7.2 Displaying Data Types
All of the invoices we created above had some prices, right? How nice would it be if we could display them nicely? Pretty insane! Well, SAP provides the functionality for this as well. To achieve this, we will start with adding a controller to the `InvoiceList.view.xml` and also modifying the `number`-attribute in the ObjectListItem:
```xml
[...]
  controllerName="sap.ui.demo.walkthrough.controller.InvoiceList"
[...]
      <ObjectListItem
        title="{invoice>Quantity} x {invoice>ProductName}"
        number="{
        parts: [{path: 'invoice>ExtendedPrice'}, {path: 'view>/currency'}],
        type: 'sap.ui.model.type.Currency',
        formatOptions: {
        showMeasure: false
        }
        }"
        numberUnit="{view>/currency}"/>
[...]
```
This new controller is called "InvoiceList", so the next step is to create it:
```javascript
sap.ui.define([
	"sap/ui/core/mvc/Controller",
	"sap/ui/model/json/JSONModel"
], function (Controller, JSONModel) {
	"use strict";

	return Controller.extend("sap.ui.demo.walkthrough.controller.InvoiceList", {

		onInit : function () {
			var oViewModel = new JSONModel({
				currency: "EUR"
			});
			this.getView().setModel(oViewModel, "view");
		}

	});
});
```
Let's explain what happens here:
 * The controller adds a new model that is called "view"
 * ObjectListItem now uses it's number attribute, which is a text attribute for things like prices that gets displayed on the right side of the list
 * The value for this attribute is built together with two different variables: the currency from the "view"-model and the ExtendedPrice from the "invoice"-model.
 * The type of number gets set to SAP-provided Currency
 * The unit of number gets set to the currency from the "view"-model

Reload your site and you should see the amount displayed beautifully.

### 7.3 Data Validation
SAP provides expression binding for data validation. It works like this:
 * ObjectListItem as an attribute called numberState
 * Expression Binding can compare variables of the models, e.g.
  ```xml
  {= ${invoice>ExtendedPrice} > 50 ? 'Error' : 'Success' }
  ```
 * numberState has different options for different values:
  * Error: Display text red
  * None: Nothing happens
  * Success: Display text green
  * Warning: Display text yellow/orange
So, whenever the price is greater than 50, the number will be displayed red (and you can probably not afford to buy that item).<br />
Remember: When using variables in expression binding, use `${}`, `&&` needs to be replaced with `&amp;&amp;`;

The official documentation for expression binding can be found [here](https://sapui5.hana.ondemand.com/#/topic/daf6852a04b44d118963968a1239d2c0.html).

### 7.4 Formatting Data
Sometimes data is stored in a rather technical format - meaning you have single characters floating around but representing a current state. The problem here is that this representation for the normal user mostly doesn't make any sense. That is the point where custom formatters join.<br />
So let's go back to our invoices we created. There was an attribute called "Status" and it was set to 'A' and 'C' (Spoiler: You can set as many statuses as you want - you just have to format all of them). Now what you're going to do is create a new file called `formatter.js` and save it in the `model` folder. What you do there is calling `sap.ui`s `define`-method with an empty array and therefore a function with empty parameters (where you don't import anything) and let the function look something like this:
```javascript
"use strict";
return {
	statusText: function (sStatus) {
		var resourceBundle = this.getView().getModel("i18n").getResourceBundle();
		switch (sStatus) {
			case "A":
				return resourceBundle.getText("invoiceStatusA");
			case "B":
				return resourceBundle.getText("invoiceStatusB");
			case "C":
				return resourceBundle.getText("invoiceStatusC");
			default:
				return sStatus;
		}
	}
};
```
As you can see it changes the status into something saved in the i18n.properties. The three added lines in the file are those:
```
invoiceStatusA=New
invoiceStatusB=In Progress
invoiceStatusC=Done
```
Now we need to set the formatter for the list, therefore update the `InvoiceList.controller.js`-file. Include the formatter (add `"sap/ui/demo/walkthrough/model/formatter"` to the array and add `formatter` to the parameters) and in the `extend`-method use a property called "formatter" and set it to the formatter (`formatter: formatter`).

The next step is to update the list that it shows the status. Therefore we add a new element in the `ObjectListItem`: `<firstStatus>`. This element includes an `<ObjectStatus>`, where the text gets displayed. The file should look something like this:
```xml
[...]
<ObjectListItem
[...]>
  <firstStatus>
    <ObjectStatus text="{
      path: 'invoice>Status',
      formatter: '.formatter.statusText'
    }"/>
  </firstStatus>
</ObjectListItem>
[...]
```
As you can see we also set the formatter and used the "invoice"-model that was set by the `manifest.json`.

### 7.5 Data Filtering
Next thing we could possibly want to do with data is filtering it. Just selecting the important parts from it. For this, we're going to add a [`<Toolbar>`](#toolbar) within a `<headerToolbar>` to the list. This toolbar is going to consist of a [`<Title>`](#title), a [`<ToolbarSpacer>`](https://sapui5.hana.ondemand.com/#/api/sap.m.ToolbarSpacer) and a [`<SearchField>`](#searchField). This last element is going to be responsible for filtering the data.


## Troubleshooting
Chrome Developer Tools -> UI5 (+ rightclick -> Inspect UI5 Control)
* `Ctrl` + `Shift` + `Alt` + `P`: Open Technical Information Dialog
* `Ctrl` + `Shift` + `Alt` + `S`: Open Diagnostic Window

### Sources
* [Hana](https://sapui5.hana.ondemand.com/#/topic/592f36fd077b45349a67dcb3efb46ab1)
