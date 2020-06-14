def generic_model_mutation_process(model, data, id=None, commit=True):
    """
    Crea y actualiza objetos en base a un model y un id.
    No tiene ningún tipo de restricción.

    :param model: Model de Django:.
    :param data: Dict con los fields para el objeto a creat/actualizar.
    :param id: Int para buscar el objeto a actualizar
    :param commit: Indica si se debe guardar el objeto.
    :return: model instance.
    """
    if id:
        item = model.objects.get(id=id)
        try:
            del data['id']
        except KeyError:
            # Sacar el id por si envían el data tal cual llega.
            pass

        for field, value in data.items():
            setattr(item, field, value)

    else:
        item = model(**data)
        # TODO: Verificaciones, auto_ids, hashing, asserts, etc.

    if commit:
        item.save()

    return item
