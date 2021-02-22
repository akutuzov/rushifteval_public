#!/usr/bin/env python3
# coding: utf-8
from __future__ import print_function
import sys
from scipy.stats import spearmanr
import os


def get_ys(model_answers, true_answers, n_answers=3):
    """
    :param model_answers: path to tab-separated answer file (lemma + "\t" + tab-separated scores)
    :param true_answers: path to tab-separated gold answer file (lemma + "\t" + tab-separated scores)
    :param n_answers: how many scores (time period pairs) for each word?
    :return: a list of the model scores, and one for the true scores
    """
    y_hat_tmp = {}
    errors = 0
    with open(model_answers, "r") as f_in:
        for line in f_in:
            res = line.strip().split("\t")
            lemma = res[0]
            y_hat_tmp[lemma] = []
            for i in range(n_answers):
                score = res[1 + i]
                if score == "nan":
                    errors += 1
                y_hat_tmp[lemma].append(float(score))
    if errors:
        print("Found %d NaN predictions" % errors, file=sys.stderr)
    y_hat, y = [], []
    with open(true_answers, "r") as f_in:
        for line in f_in:
            res = line.strip().split("\t")
            lemma = res[0]
            scores = []
            for i in range(n_answers):
                score = res[1 + i]
                scores.append(float(score))
            try:
                predicted_answer = y_hat_tmp[lemma]
            except KeyError:
                raise SystemExit("Error: the word %s not found in the submission!" % lemma)
            assert len(predicted_answer) == len(scores)
            y.append(scores)
            y_hat.append(predicted_answer)

    return y_hat, y


def eval_task2(model_answers, true_answers):
    """
    Computes the Spearman's correlation coefficient against the true rank as annotated by humans
    :param model_answers: list of scores' lists
    :param true_answers: list of scores' lists
    :return: (Spearman's correlation coefficient, p-value)
    """
    assert len(model_answers[0]) == len(true_answers[0])
    nr_scores = len(true_answers[0])
    correlations = []
    for i in range(nr_scores):
        cur_preds = [el[i] for el in model_answers]
        cur_golds = [el[i] for el in true_answers]
        r, p = spearmanr(cur_preds, cur_golds, nan_policy="omit")
        correlations.append((r, p))
    return correlations


def main():
    """
    Evaluate lexical semantic change detection results.
    """
    input_dir = sys.argv[1]
    output_dir = sys.argv[2]

    submit_dir = os.path.join(input_dir, "res")
    truth_dir = os.path.join(input_dir, "ref")

    if not os.path.isdir(submit_dir):
        print("%s doesn't exist" % submit_dir)

    if os.path.isdir(submit_dir) and os.path.isdir(truth_dir):
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    output_filename = os.path.join(output_dir, "scores.txt")
    output_file = open(output_filename, "w")

    truth_file = os.path.join(truth_dir, "truth.tsv")

    submission_answer_file = os.path.join(submit_dir, "answer.tsv")

    predictions, gold = get_ys(submission_answer_file, truth_file)
    res = eval_task2(predictions, gold)
    print("Spearman rho score 0: {:.3f}  p: {:.3f}".format(res[0][0], res[0][1]))
    print("Spearman rho score 1: {:.3f}  p: {:.3f}".format(res[1][0], res[1][1]))
    print("Spearman rho score 2: {:.3f}  p: {:.3f}".format(res[2][0], res[2][1]))
    ave_score = (res[0][0] + res[1][0] + res[2][0]) / 3
    print("Average score: {:.3f}".format(ave_score))
    output_file.write("spearman0: {:.3f}\n".format(res[0][0]))
    output_file.write("spearman1: {:.3f}\n".format(res[1][0]))
    output_file.write("spearman2: {:.3f}\n".format(res[2][0]))
    output_file.write("ave_score: {:.3f}\n".format(ave_score))


if __name__ == "__main__":
    main()
