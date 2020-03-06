package sample;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

public class Main extends Application {

    @Override
    public void start(Stage primaryStage) throws Exception {
        FXMLLoader mainLoader = new FXMLLoader();
        mainLoader.setLocation(getClass().getResource("PrgView.fxml"));
        Parent mainWindow = mainLoader.load();

        PrgViewCtrl mainWindowController = mainLoader.getController();

        primaryStage.setTitle("Main Window");
        primaryStage.setScene(new Scene(mainWindow));
        primaryStage.show();

        FXMLLoader secondaryLoader = new FXMLLoader();
        secondaryLoader.setLocation(getClass().getResource("programsWindow.fxml"));
        Parent secondaryWindow = secondaryLoader.load();

        programsWindow selectWindowController = secondaryLoader.getController();
        selectWindowController.setPrgViewCtrl(mainWindowController);
        Stage secondaryStage = new Stage();
        secondaryStage.setTitle("Select Window");
        secondaryStage.setScene(new Scene(secondaryWindow));
        secondaryStage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
