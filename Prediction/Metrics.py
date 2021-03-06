from sklearn.metrics import f1_score, precision_score, recall_score, accuracy_score, classification_report, \
    brier_score_loss, auc, confusion_matrix, roc_auc_score, precision_recall_curve, cohen_kappa_score


def brier(preds, dtrain):
   labels = dtrain.get_label()
   preds = 1.0 / (1.0 + np.exp(-preds))
   grad = 2*(preds-labels)*preds*(1-preds)
   hess = 2*(2*(labels+1)*preds-labels-3*preds*preds)*preds*(1-preds)
   return grad, hess


def performance_metrics(testing_y, y_pred_binary,prediction_probabilities):
    F1Macro = f1_score(testing_y, y_pred_binary, average='macro')
    PrecisionMacro = precision_score(testing_y, y_pred_binary, average='macro')
    RecallMacro = recall_score(testing_y, y_pred_binary, average='macro')
    Accuracy = accuracy_score(testing_y, y_pred_binary)
    BS = brier_score_loss(testing_y, prediction_probabilities)
    CK = cohen_kappa_score(testing_y, y_pred_binary)
    ClassificationReport = classification_report(testing_y, y_pred_binary)
    CM = confusion_matrix(testing_y, y_pred_binary)

    TN = CM[0][0]
    FN = CM[1][0]
    TP = CM[1][1]
    FP = CM[0][1]

    PPV = TP/(TP+FP)
    NPV = TN/(TN+FN)

    roc_auc = roc_auc_score(testing_y, y_pred_binary)
    precision_rt, recall_rt, threshold_rt = precision_recall_curve(testing_y,
                                                                   y_pred_binary)
    #pr_auc = auc(precision_rt, recall_rt)

    performance_row = {
        "F1-Macro" : F1Macro,
        "Precision-Macro" : PrecisionMacro,
        "Recall-Macro" : RecallMacro,
        "Accuracy" : Accuracy,
        "ClassificationReport" : ClassificationReport,
        "PPV":PPV,
        "NPV":NPV,
        "TP":TP,
        "FP":FP,
        "TN":TN,
        "FN":FN,
        "ROC-AUC":roc_auc,
        #"PR-AUC" : pr_auc,
        "Brier-Score": BS,
        "Cohen's Kappa":CK
        #"PR-AUC": pr_auc
    }

    return performance_row

