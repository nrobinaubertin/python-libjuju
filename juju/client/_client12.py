# DO NOT CHANGE THIS FILE! This file is auto-generated by facade.py.
# Changes will be overwritten/lost when the file is regenerated.

from juju.client._definitions import *
from juju.client.facade import ReturnMapping, Type


class ControllerFacade(Type):
    name = "Controller"
    version = 12

    @ReturnMapping(UserModelList)
    async def AllModels(self):
        """AllModels allows controller administrators to get the list of all the
        models in the controller.

        Returns -> UserModelList
        """
        # map input types to rpc msg
        _params = dict()
        msg = dict(type="Controller", request="AllModels", version=12, params=_params)

        reply = await self.rpc(msg)
        return reply

    @ReturnMapping(CloudSpecResults)
    async def CloudSpec(self, entities=None):
        """CloudSpec returns the model's cloud spec.

        entities : typing.Sequence[~Entity]
        Returns -> CloudSpecResults
        """
        if entities is not None and not isinstance(entities, (bytes, str, list)):
            raise Exception(
                f"Expected entities to be a Sequence, received: {type(entities)}"
            )

        # map input types to rpc msg
        _params = dict()
        msg = dict(type="Controller", request="CloudSpec", version=12, params=_params)
        _params["entities"] = entities
        reply = await self.rpc(msg)
        return reply

    @ReturnMapping(None)
    async def ConfigSet(self, config=None):
        """ConfigSet changes the value of specified controller configuration
        settings. Only some settings can be changed after bootstrap.
        Settings that aren't specified in the params are left unchanged.

        config : typing.Mapping[str, typing.Any]
        Returns -> None
        """
        if config is not None and not isinstance(config, dict):
            raise Exception(
                f"Expected config to be a Mapping, received: {type(config)}"
            )

        # map input types to rpc msg
        _params = dict()
        msg = dict(type="Controller", request="ConfigSet", version=12, params=_params)
        _params["config"] = config
        reply = await self.rpc(msg)
        return reply

    @ReturnMapping(ControllerAPIInfoResults)
    async def ControllerAPIInfoForModels(self, entities=None):
        """ControllerAPIInfoForModels returns the controller api connection details for the specified models.

        entities : typing.Sequence[~Entity]
        Returns -> ControllerAPIInfoResults
        """
        if entities is not None and not isinstance(entities, (bytes, str, list)):
            raise Exception(
                f"Expected entities to be a Sequence, received: {type(entities)}"
            )

        # map input types to rpc msg
        _params = dict()
        msg = dict(
            type="Controller",
            request="ControllerAPIInfoForModels",
            version=12,
            params=_params,
        )
        _params["entities"] = entities
        reply = await self.rpc(msg)
        return reply

    @ReturnMapping(ControllerConfigResult)
    async def ControllerConfig(self):
        """ControllerConfig returns the controller's configuration.

        Returns -> ControllerConfigResult
        """
        # map input types to rpc msg
        _params = dict()
        msg = dict(
            type="Controller", request="ControllerConfig", version=12, params=_params
        )

        reply = await self.rpc(msg)
        return reply

    @ReturnMapping(ControllerVersionResults)
    async def ControllerVersion(self):
        """ControllerVersion returns the version information associated with this
        controller binary.

        NOTE: the implementation intentionally does not check for SuperuserAccess
        as the Version is known even to users with login access.

        Returns -> ControllerVersionResults
        """
        # map input types to rpc msg
        _params = dict()
        msg = dict(
            type="Controller", request="ControllerVersion", version=12, params=_params
        )

        reply = await self.rpc(msg)
        return reply

    @ReturnMapping(DashboardConnectionInfo)
    async def DashboardConnectionInfo(self):
        """DashboardConnectionInfo returns the connection information for a client to
        connect to the Juju Dashboard including any proxying information.

        Returns -> DashboardConnectionInfo
        """
        # map input types to rpc msg
        _params = dict()
        msg = dict(
            type="Controller",
            request="DashboardConnectionInfo",
            version=12,
            params=_params,
        )

        reply = await self.rpc(msg)
        return reply

    @ReturnMapping(None)
    async def DestroyController(
        self,
        destroy_models=None,
        destroy_storage=None,
        force=None,
        max_wait=None,
        model_timeout=None,
    ):
        """DestroyController destroys the controller.

        If the args specify the destruction of the models, this method will
        attempt to do so. Otherwise, if the controller has any non-empty,
        non-Dead hosted models, then an error with the code
        params.CodeHasHostedModels will be transmitted.

        destroy_models : bool
        destroy_storage : bool
        force : bool
        max_wait : int
        model_timeout : int
        Returns -> None
        """
        if destroy_models is not None and not isinstance(destroy_models, bool):
            raise Exception(
                f"Expected destroy_models to be a bool, received: {type(destroy_models)}"
            )

        if destroy_storage is not None and not isinstance(destroy_storage, bool):
            raise Exception(
                f"Expected destroy_storage to be a bool, received: {type(destroy_storage)}"
            )

        if force is not None and not isinstance(force, bool):
            raise Exception(f"Expected force to be a bool, received: {type(force)}")

        if max_wait is not None and not isinstance(max_wait, int):
            raise Exception(
                f"Expected max_wait to be a int, received: {type(max_wait)}"
            )

        if model_timeout is not None and not isinstance(model_timeout, int):
            raise Exception(
                f"Expected model_timeout to be a int, received: {type(model_timeout)}"
            )

        # map input types to rpc msg
        _params = dict()
        msg = dict(
            type="Controller", request="DestroyController", version=12, params=_params
        )
        _params["destroy-models"] = destroy_models
        _params["destroy-storage"] = destroy_storage
        _params["force"] = force
        _params["max-wait"] = max_wait
        _params["model-timeout"] = model_timeout
        reply = await self.rpc(msg)
        return reply

    @ReturnMapping(CloudSpecResult)
    async def GetCloudSpec(self):
        """GetCloudSpec constructs the CloudSpec for a validated and authorized model.

        Returns -> CloudSpecResult
        """
        # map input types to rpc msg
        _params = dict()
        msg = dict(
            type="Controller", request="GetCloudSpec", version=12, params=_params
        )

        reply = await self.rpc(msg)
        return reply

    @ReturnMapping(UserAccessResults)
    async def GetControllerAccess(self, entities=None):
        """GetControllerAccess returns the level of access the specified users
        have on the controller.

        entities : typing.Sequence[~Entity]
        Returns -> UserAccessResults
        """
        if entities is not None and not isinstance(entities, (bytes, str, list)):
            raise Exception(
                f"Expected entities to be a Sequence, received: {type(entities)}"
            )

        # map input types to rpc msg
        _params = dict()
        msg = dict(
            type="Controller", request="GetControllerAccess", version=12, params=_params
        )
        _params["entities"] = entities
        reply = await self.rpc(msg)
        return reply

    @ReturnMapping(HostedModelConfigsResults)
    async def HostedModelConfigs(self):
        """HostedModelConfigs returns all the information that the client needs in
        order to connect directly with the host model's provider and destroy it
        directly.

        Returns -> HostedModelConfigsResults
        """
        # map input types to rpc msg
        _params = dict()
        msg = dict(
            type="Controller", request="HostedModelConfigs", version=12, params=_params
        )

        reply = await self.rpc(msg)
        return reply

    @ReturnMapping(StringResult)
    async def IdentityProviderURL(self):
        """IdentityProviderURL returns the URL of the configured external identity
        provider for this controller or an empty string if no external identity
        provider has been configured when the controller was bootstrapped.

        NOTE: the implementation intentionally does not check for SuperuserAccess
        as the URL is known even to users with login access.

        Returns -> StringResult
        """
        # map input types to rpc msg
        _params = dict()
        msg = dict(
            type="Controller", request="IdentityProviderURL", version=12, params=_params
        )

        reply = await self.rpc(msg)
        return reply

    @ReturnMapping(InitiateMigrationResults)
    async def InitiateMigration(self, specs=None):
        """InitiateMigration attempts to begin the migration of one or
        more models to other controllers.

        specs : typing.Sequence[~MigrationSpec]
        Returns -> InitiateMigrationResults
        """
        if specs is not None and not isinstance(specs, (bytes, str, list)):
            raise Exception(f"Expected specs to be a Sequence, received: {type(specs)}")

        # map input types to rpc msg
        _params = dict()
        msg = dict(
            type="Controller", request="InitiateMigration", version=12, params=_params
        )
        _params["specs"] = specs
        reply = await self.rpc(msg)
        return reply

    @ReturnMapping(ModelBlockInfoList)
    async def ListBlockedModels(self):
        """ListBlockedModels returns a list of all models on the controller
        which have a block in place.  The resulting slice is sorted by model
        name, then owner. Callers must be controller administrators to retrieve the
        list.

        Returns -> ModelBlockInfoList
        """
        # map input types to rpc msg
        _params = dict()
        msg = dict(
            type="Controller", request="ListBlockedModels", version=12, params=_params
        )

        reply = await self.rpc(msg)
        return reply

    @ReturnMapping(ModelStatusResults)
    async def ModelStatus(self, entities=None):
        """ModelStatus returns a summary of the model.

        entities : typing.Sequence[~Entity]
        Returns -> ModelStatusResults
        """
        if entities is not None and not isinstance(entities, (bytes, str, list)):
            raise Exception(
                f"Expected entities to be a Sequence, received: {type(entities)}"
            )

        # map input types to rpc msg
        _params = dict()
        msg = dict(type="Controller", request="ModelStatus", version=12, params=_params)
        _params["entities"] = entities
        reply = await self.rpc(msg)
        return reply

    @ReturnMapping(ErrorResults)
    async def ModifyControllerAccess(self, changes=None):
        """ModifyControllerAccess changes the model access granted to users.

        changes : typing.Sequence[~ModifyControllerAccess]
        Returns -> ErrorResults
        """
        if changes is not None and not isinstance(changes, (bytes, str, list)):
            raise Exception(
                f"Expected changes to be a Sequence, received: {type(changes)}"
            )

        # map input types to rpc msg
        _params = dict()
        msg = dict(
            type="Controller",
            request="ModifyControllerAccess",
            version=12,
            params=_params,
        )
        _params["changes"] = changes
        reply = await self.rpc(msg)
        return reply

    @ReturnMapping(StringResult)
    async def MongoVersion(self):
        """MongoVersion allows the introspection of the mongo version per controller

        Returns -> StringResult
        """
        # map input types to rpc msg
        _params = dict()
        msg = dict(
            type="Controller", request="MongoVersion", version=12, params=_params
        )

        reply = await self.rpc(msg)
        return reply

    @ReturnMapping(None)
    async def RemoveBlocks(self, all_=None):
        """RemoveBlocks removes all the blocks in the controller.

        all_ : bool
        Returns -> None
        """
        if all_ is not None and not isinstance(all_, bool):
            raise Exception(f"Expected all_ to be a bool, received: {type(all_)}")

        # map input types to rpc msg
        _params = dict()
        msg = dict(
            type="Controller", request="RemoveBlocks", version=12, params=_params
        )
        _params["all"] = all_
        reply = await self.rpc(msg)
        return reply

    @ReturnMapping(SummaryWatcherID)
    async def WatchAllModelSummaries(self):
        """WatchAllModelSummaries starts watching the summary updates from the cache.
        This method is superuser access only, and watches all models in the
        controller.

        Returns -> SummaryWatcherID
        """
        # map input types to rpc msg
        _params = dict()
        msg = dict(
            type="Controller",
            request="WatchAllModelSummaries",
            version=12,
            params=_params,
        )

        reply = await self.rpc(msg)
        return reply

    @ReturnMapping(AllWatcherId)
    async def WatchAllModels(self):
        """WatchAllModels starts watching events for all models in the
        controller. The returned AllWatcherId should be used with Next on the
        AllModelWatcher endpoint to receive deltas.

        Returns -> AllWatcherId
        """
        # map input types to rpc msg
        _params = dict()
        msg = dict(
            type="Controller", request="WatchAllModels", version=12, params=_params
        )

        reply = await self.rpc(msg)
        return reply

    @ReturnMapping(NotifyWatchResults)
    async def WatchCloudSpecsChanges(self, entities=None):
        """WatchCloudSpecsChanges returns a watcher for cloud spec changes.

        entities : typing.Sequence[~Entity]
        Returns -> NotifyWatchResults
        """
        if entities is not None and not isinstance(entities, (bytes, str, list)):
            raise Exception(
                f"Expected entities to be a Sequence, received: {type(entities)}"
            )

        # map input types to rpc msg
        _params = dict()
        msg = dict(
            type="Controller",
            request="WatchCloudSpecsChanges",
            version=12,
            params=_params,
        )
        _params["entities"] = entities
        reply = await self.rpc(msg)
        return reply

    @ReturnMapping(SummaryWatcherID)
    async def WatchModelSummaries(self):
        """WatchModelSummaries starts watching the summary updates from the cache.
        Only models that the user has access to are returned.

        Returns -> SummaryWatcherID
        """
        # map input types to rpc msg
        _params = dict()
        msg = dict(
            type="Controller", request="WatchModelSummaries", version=12, params=_params
        )

        reply = await self.rpc(msg)
        return reply